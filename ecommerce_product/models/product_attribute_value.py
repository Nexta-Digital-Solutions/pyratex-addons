from odoo import api, fields, models, _

class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'

    icon_id = fields.Binary(string='Icono')
    colorgroup_id = fields.Many2one('color.group', string='Group')
    attribute_name = fields.Char(related="attribute_id.name", string="Attribute Name")
