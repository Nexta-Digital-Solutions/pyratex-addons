from odoo import api, fields, models, _


class Certifications(models.Model):
    _name = 'product.product.certifications'
    _description = 'Modelo para añadir certificados'

    name = fields.Char(string='Nombre')
    image = fields.Binary(string='Imagen')

