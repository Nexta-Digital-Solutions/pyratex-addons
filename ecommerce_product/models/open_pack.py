from odoo import api, fields, models, _


class OpenPack(models.Model):
    _name = 'open.pack'
    _description = 'Modelo para añadir Packs abiertos'

    pack_name = fields.Char(string='Nombre del Pack')
    price = fields.Char(string='Precio')
    elements_number = fields.Integer(string='Número de elementos')