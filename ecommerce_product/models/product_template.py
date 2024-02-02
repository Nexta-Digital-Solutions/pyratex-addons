from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # composition_id = fields.Many2many('product.composition', string='Composition')
    country_id = fields.Many2one('res.country', string='Made in')
    weight = fields.Char(string='Weight')
    width = fields.Char(string='Width')
    description_ecommerce = fields.Text(string='Ecommerce Sales Description')
    fiberfamily_id = fields.Many2one('fiber.family', string='Fiber Family')