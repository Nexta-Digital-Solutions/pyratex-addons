from odoo import api, fields, models, _


class OpenPack(models.Model):
    _name = 'open.pack'
    _description = 'Modelo para añadir Packs abiertos'

    name = fields.Char(string='Nombre del Pack')
    price = fields.Float(string='Precio')
    elements_number = fields.Integer(string='Número de elementos')