from odoo import api, fields, models, _

class ProductComposition(models.Model):
    _name = 'product.composition'
    _description = 'Creación de la tabla Composición con el campo.'

    name = fields.Char(string='Composition')