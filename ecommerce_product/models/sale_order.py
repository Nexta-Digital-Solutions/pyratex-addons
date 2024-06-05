from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def create_so_website(self, product_tmp_id, price):
        return self.env['sale.order'].create({
            'partner_id': self.partner_id.id,
            'date_order': self.date_order,
            'order_line': self.order_line
        })

    def _prepare_order_line_update_values(self, order_line, quantity, linked_line_id=False, **kwargs):
        values = super()._prepare_order_line_update_values(order_line, quantity, linked_line_id, **kwargs)
        if 'price_unit' in kwargs:
            values["price_unit"] = kwargs.get('price_unit')
        return values