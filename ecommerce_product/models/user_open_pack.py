from odoo import api, fields, models, _


class UserOpenPack(models.Model):
    _name = 'user.open.pack'
    _description = 'Modelo para añadir los usuarios con el pack abierto'

    user_id = fields.Many2one('res.users', string='Usuario')
    product_template_id = fields.Many2one('product.template', string='Product')
    pack_name_id = fields.Many2one('open.pack', string='Pack')