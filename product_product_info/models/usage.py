
from odoo import api, fields, models, _

class Usage(models.Model):
    _name = 'product.product.usage'
    _description = 'Modelo para añadir la forma de empleo'

    name = fields.Char(string='Nombre')
    image = fields.Binary(string='Imagen')
