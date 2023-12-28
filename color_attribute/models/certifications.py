from odoo import api, fields, models, _


class Certifications(models.Model):
    _name = 'product.product.certifications'

    name = fields.Char(string='Nombre')
    image = fields.Binary(string='Imagen')

