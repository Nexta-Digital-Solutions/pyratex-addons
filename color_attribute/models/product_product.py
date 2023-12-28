from odoo import api, fields, models, _

class ProductProduct(models.Model):
    _inherit = 'product.template'

    fiberfamily_id = fields.Many2one('product.product.fiberfamily', string='Fiber Family')
    property_id = fields.Many2one('product.product.properties', string='Property')
    usage_id = fields.Many2many(comodel_name='product.product.usage', string='Usage')
    certification_id = fields.Many2many(comodel_name='product.product.certifications', string='Certifications')