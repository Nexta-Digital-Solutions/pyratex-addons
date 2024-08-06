# -*- coding: utf-8 -*-

from collections import defaultdict
from itertools import product as cartesian_product
import json
import logging
from datetime import datetime
from werkzeug.exceptions import Forbidden, NotFound
from werkzeug.urls import url_decode, url_encode, url_parse

from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.fields import Command
from odoo.http import request
from odoo.addons.base.models.ir_qweb_fields import nl2br
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.ecommerce_filter.controllers.website_sale_products import ProductsFilter
from odoo.addons.payment import utils as payment_utils
from odoo.tools.json import scriptsafe as json_scriptsafe

class WebsiteSaleCart(ProductsFilter):
    @http.route(['/shop/cart/update_json'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update_json(
        self, product_id, line_id=None, add_qty=None, set_qty=None, display=True,
        product_custom_attribute_values=None, no_variant_attribute_values=None, price_unit = None,**kw
    ):
        order = request.website.sale_get_order(force_create=True)
        if order.state != 'draft':
            request.website.sale_reset()
            if kw.get('force_create'):
                order = request.website.sale_get_order(force_create=True)
            else:
                return {}

        if product_custom_attribute_values:
            product_custom_attribute_values = json_scriptsafe.loads(product_custom_attribute_values)

        if no_variant_attribute_values:
            no_variant_attribute_values = json_scriptsafe.loads(no_variant_attribute_values)

        values = order._cart_update(
            product_id=product_id,
            line_id=line_id,
            add_qty=add_qty,
            set_qty=set_qty,
            product_custom_attribute_values=product_custom_attribute_values,
            no_variant_attribute_values=no_variant_attribute_values,
            **kw
        )
        
        """type_of_order: prevalece el de fabrics"""
        saleorder_line_ids = order.order_line if order.order_line else False
        if (saleorder_line_ids and set_qty > 0):
            type_of_order_fabrics = saleorder_line_ids.filtered(lambda x: x.product_id.product_tmpl_id.producttype_id.name.lower() == "fabrics")
            type_of_order = type_of_order_fabrics[0].product_id.product_tmpl_id.producttype_id.type_of_order \
                            if type_of_order_fabrics else saleorder_line_ids[0].product_id.product_tmpl_id.producttype_id.type_of_order if  order.order_line else False
            order.update({
                'x_studio_type_of_order': type_of_order if not order.x_studio_type_of_order else order.x_studio_type_of_order
            })
        
        if (price_unit):
            line_id = request.env['sale.order.line'].browse(values['line_id'])
            price_reduce = price_unit / (1 + line_id.tax_id.amount /100 )
            line_id.update ({
                'price_reduce': price_reduce,
                'price_tax': float(price_unit - price_reduce),
                'price_subtotal': float(price_reduce),
                'price_total': line_id.product_qty * float(price_reduce)
            })

        """ Incremento el precio del product Fabric - añadir 25 % adicional al pvp"""
        is_fabric = request.env['product.product'].search([ ('id','=', product_id), ('producttype_id.name','ilike','fabric') ])
        if (is_fabric):
            line_id = request.env['sale.order.line'].browse(values['line_id'])
            price_unit = line_id.price_unit
            percentage_additional = int(request.env['ir.config_parameter'].get_param('Fabric Percentage', 1))
            price_reduce = price_unit * (1 + percentage_additional / 100) / (1 + line_id.tax_id.amount /100 )
            line_id.update ({
                'price_reduce': price_reduce,
                'price_tax': float(price_unit - price_reduce),
                'price_subtotal': float(price_reduce),
                'price_total': line_id.product_qty * float(price_reduce)
            })

        request.session['website_sale_cart_quantity'] = order.cart_quantity

        if not order.cart_quantity:
            request.website.sale_reset()
            return values

        parent_pack = request.env['product.product'].search([('name', '=', 'Swatches')], limit=1)
        if parent_pack and product_id == parent_pack.id and (set_qty == 0 or (add_qty and values['quantity'] == 0)):
            swatches_lines = order.order_line.filtered(lambda l: l.product_id.producttype_id.name == "Swatches")
            for line in swatches_lines:
                line.unlink()

        request.session['website_sale_cart_quantity'] = order.cart_quantity

        values['cart_quantity'] = order.cart_quantity
        values['minor_amount'] = payment_utils.to_minor_currency_units(
            order.amount_total, order.currency_id
        ),
        values['amount'] = order.amount_total

        if not display:
            return values

        values['website_sale.cart_lines'] = request.env['ir.ui.view']._render_template(
            "website_sale.cart_lines", {
                'website_sale_order': order,
                'date': fields.Date.today(),
                'suggested_products': order._cart_accessories()
            }
        )
        values['website_sale.short_cart_summary'] = request.env['ir.ui.view']._render_template(
            "website_sale.short_cart_summary", {
                'website_sale_order': order,
            }
        )
        return values