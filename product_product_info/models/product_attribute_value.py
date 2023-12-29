from odoo import api, fields, models, _


class ProductAttribute(models.Model):
    _inherit = 'product.attribute.value'

    group_id = fields.Many2one('product.attribute.group', string='Group')

