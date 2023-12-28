
from odoo import api, fields, models, _


class Properties(models.Model):
    _name = 'product.product.properties'
    _description = 'Modelo para añadir propiedades'

    name = fields.Char(string='Nombre')
    image = fields.Char(string='Imagen')


