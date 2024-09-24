from odoo import api, fields, models, _
from odoo.fields import Command

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    check_price = fields.Boolean(string = "Check Price", help = "To check price for 25% increment to fabrics product")