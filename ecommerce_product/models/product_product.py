from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit = 'product.product'

    # colorgroup_id = fields.Many2one('product.attribute.value', string='Color Groups', readonly=False, domain="[('attribute_id.name', '=', 'Color')]",)
    # colorgroup_id = fields.Many2one('color.group', string='Color Groups', readonly=False, domain="[('product_attribute_valued_ids.attribute_id.name', '=', 'Color')]", relate="product_attribute_valued_ids.colorgroup_id")

    colorgroup_id = fields.Many2one('color.group', string='Color Groups', compute='_compute_colorgroup_ids',
                                       readonly=False)

    @api.depends('attribute_line_ids', 'attribute_line_ids.colorgroup_id')
    def _compute_colorgroup_ids(self):
        for template in self:
            color_groups = template.attribute_line_ids.mapped('colorgroup_id')
            if color_groups:
                template.colorgroup_id = color_groups[0]
            else:
                template.colorgroup_id = False

