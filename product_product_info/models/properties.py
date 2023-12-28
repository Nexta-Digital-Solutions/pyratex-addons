
from odoo import api, fields, models, _


class Properties(models.Model):
    _name = 'product.product.properties'

    name = fields.Char(string='Nombre')
    image = fields.Char(string='Imagen')


