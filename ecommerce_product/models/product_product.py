from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit = 'product.template'

    composition_id = fields.Many2many('product.composition', string='Composition')
