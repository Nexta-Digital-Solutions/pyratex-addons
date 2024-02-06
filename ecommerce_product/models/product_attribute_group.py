from odoo import api, fields, models, _


class ProductAttributeGroup(models.Model):
    _name = 'product.attribute.group'
    _description = 'Grupo es utilizado para englobar colores'

    name = fields.Char(string='Group')