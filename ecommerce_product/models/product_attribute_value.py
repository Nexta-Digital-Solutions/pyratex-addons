from odoo import api, fields, models, _

class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'

    icon_id = fields.Binary(string='Icono')