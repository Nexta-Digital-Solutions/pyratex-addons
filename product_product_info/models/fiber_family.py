
from odoo import api, fields, models, _


class FiberFamily(models.Model):
    _name = 'product.product.fiberfamily'

    name = fields.Char(string='Nombre')

