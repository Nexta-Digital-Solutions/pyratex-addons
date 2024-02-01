from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import fields, http, SUPERUSER_ID, tools, _


class ProductsFilter(WebsiteSale, http.Controller):
    # def _get_search_options(
    #         self, category=None, attrib_values=None, pricelist=None, min_price=0.0, max_price=0.0, conversion_rate=1,
    #         **post
    # ):
    #     res = super(ProductsFilter, self)._get_search_options(category, attrib_values, pricelist, min_price, max_price, conversion_rate,
    #                                       **post)
    #     if post.get('fiberfamily'):
    #         res['fiberfamily'] = post.get('fiberfamily')
    #     return res

    def _get_search_options(
            self, category=None, attrib_values=None, pricelist=None, min_price=0.0, max_price=0.0, conversion_rate=1,
            **post
    ):
        res = {
            'displayDescription': True,
            'displayDetail': True,
            'displayExtraDetail': True,
            'displayExtraLink': True,
            'displayImage': True,
            'allowFuzzy': not post.get('noFuzzy'),
            'category': str(category.id) if category else None,
            'min_price': min_price / conversion_rate,
            'max_price': max_price / conversion_rate,
            'attrib_values': attrib_values,
            'display_currency': pricelist.currency_id,
        }

        if post.get('fiberfamily'):
            res['fiberfamily'] = post.get('fiberfamily')

        return res
