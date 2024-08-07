# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, http, tools, _
from odoo.http import request



class WebsiteSale(http.Controller):

    @http.route(['/shop/clear_cart'], type='http', auth="public", website=True)
    def clear_cart(self):
        order = request.website.sale_get_order()
        if order:
            for line in order.website_order_line:
                if line.exists() and line.product_id.name == 'consu':
                    line.unlink()
        return request.redirect('/shop/cart')
