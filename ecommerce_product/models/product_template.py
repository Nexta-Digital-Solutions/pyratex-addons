from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    country_id = fields.Many2one('res.country', string='Made in')
    weight = fields.Float(string='Weight', digits = (4,2))
    width = fields.Float(string='Width', digits = (4,2))
    description_ecommerce = fields.Text(string='Ecommerce Sales Description')
    fiberfamily_id = fields.Many2one('fiber.family', string='Fiber Family')
    property_id = fields.Many2many('properties', string='Property')
    usage_id = fields.Many2many('usage', string='Usage')
    producttype_id = fields.Many2one('product.type', string='Product Type')
    structure_id = fields.Many2one('structure', string='Structure')
    careinstructions_id = fields.Many2many('care.instructions', string='Care Instructions')
    certification_id = fields.Many2many('certification', string='Certification')
    composition_id = fields.Many2many('composition', string='Composition')


