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

        order_lines = order_line.order_id.order_line
        all_swatches = all(line.product_id.producttype_id and line.product_id.producttype_id.name == "Swatches" or
                           line.product_id.producttype_id.name == "Swatchpacks" for line in order_lines)
        # all_stock = all(line.product_id.producttype_id and line.product_id.producttype_id.name == "Swatches" or
        #                          line.product_id.producttype_id.name == "Fabrics" for line in order_lines)


        # ATENCION SOLO FALLA EN LOCAL!!!!
        if all_swatches:
            values["x_studio_type_of_order"] = "e-shop Swatches"
        else:
            values["x_studio_type_of_order"] = "e-shop Stock"
        return values

class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    x_studio_type_of_order = fields.Selection(string='Type of order', related='order_id.x_studio_type_of_order')