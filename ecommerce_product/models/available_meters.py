
from odoo import api, fields, models, _


class AvailableMeters(models.Model):
    _name = 'product.available.meters'
    _description = 'Modelo para añadir propiedades de Available Meters'

    name = fields.Integer(string='Name')
    min = fields.Integer(string='Mínimo')
    max = fields.Integer(string='Máximo')
