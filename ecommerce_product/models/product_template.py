from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # composition_id = fields.Many2many('product.composition', string='Composition')
    country_id = fields.Many2one('res.country', string='Made in')