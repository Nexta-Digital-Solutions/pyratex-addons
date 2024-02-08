
from odoo import api, fields, models, _


class AvailableMeters(models.Model):
    _name = 'available.meters'
    _description = 'Modelo para añadir propiedades de Available Meters'

    under_fifteen = fields.Char(string='Under 15m')
    under_fifty = fields.Char(string='Under 50m')
    over_fifty = fields.Char(string='Over 50m')
