from odoo import api, fields, models, _


class ColorGroup(models.Model):
    _name = 'color.group'
    _description = 'Grupo es utilizado para englobar colores'

    name = fields.Char(string='Group')