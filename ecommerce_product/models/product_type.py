
from odoo import api, fields, models, _


class ProductType(models.Model):
    _name = 'product.type'
    _description = 'Modelo para añadir tres tipos de productos'

    name = fields.Char(string='Nombre')