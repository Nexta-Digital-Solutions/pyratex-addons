
from odoo import api, fields, models, _

class Usage(models.Model):
    _name = 'product.product.usage'

    name = fields.Char(string='Nombre')
    image = fields.Char(string='Imagen')
