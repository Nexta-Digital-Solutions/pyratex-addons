# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class WebsiteAddMultiProduct(http.Controller):
    @http.route('/shop/cart/add_multi_product', type='http', auth="public",
                methods=['GET'], website=True)
    def cart_add_multi_product(self, **kw):
        sale_order = request.website.sale_get_order(force_create=True)
        for product_ids in kw.values():
            if product_ids:
                product_id = int(product_ids)
                order_line = sale_order.order_line.filtered(
                    lambda line: line.product_id.id == product_id)
                if order_line:
                    order_line.product_uom_qty += 1
                else:
                    sale_order._cart_update(
                        product_id=product_id,
                        add_qty=1,
                        set_qty=1,
                    )
            request.session['website_sale_cart_quantity'] = (
                sale_order.cart_quantity)

    @http.route(['/shop/cart/qty'], type='json', auth="public",
                methods=['POST'], website=True, csrf=False)
    def cart_qty_check(self):
        cart_qty = request.website.sale_get_order().cart_quantity
        request.session['website_sale_cart_quantity'] = cart_qty
        return request.session['website_sale_cart_quantity']
