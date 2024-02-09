from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    country_id = fields.Many2one('res.country', string='Made in')
    weight = fields.Char(string='Weight')
    width = fields.Char(string='Width')
    description_ecommerce = fields.Text(string='Ecommerce Sales Description')
    fiberfamily_id = fields.Many2one('fiber.family', string='Fiber Family')
    property_id = fields.Many2many('properties', string='Property')
    usage_id = fields.Many2many('usage', string='Usage')
    producttype_id = fields.Many2one('product.type', string='Product Type')
    structure_id = fields.Many2one('structure', string='Structure')
    careinstructions_id = fields.Many2many('care.instructions', string='Care Instructions')
    certification_id = fields.Many2many('certification', string='Certification')
    is_published = fields.Boolean(copy=False)

    # colorgroup_id = fields.Many2many('color.group', string='Color Groups', compute='_compute_colorgroup_ids',
    #                                   store=True, readonly=False)
    #
    # @api.depends('attribute_line_ids')
    # def _compute_colorgroup_ids(self):
    #     for template in self:
    #         color_groups = template.attribute_line_ids.mapped('colorgroup_id')
    #         template.colorgroup_id = color_groups

