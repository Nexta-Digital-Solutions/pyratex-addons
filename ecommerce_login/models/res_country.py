from odoo import fields, models, _


class ResCountryWebsite(models.Model):
    _inherit = 'res.country'
    
    not_show_website = fields.Boolean(string = "Not show Website")