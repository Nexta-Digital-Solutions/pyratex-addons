from odoo import fields, models, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    profession = fields.Selection([('individual', 'An Individual'), ('student', 'A Student'), ('company', 'A Company'), ('library','A Material Library'), ('project','Starting a new project')], string='Profession')
    about_us = fields.Selection([('engine', 'Search engine'), ('instagram', 'Instagram'), ('linkedin', 'Linkedin'), ('word','Word of Mouth'), ('events','Events'), ('newspaper', 'Newspaper/ Press'),('other','Other')], string='Profession')
