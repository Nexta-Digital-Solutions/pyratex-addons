# -*- coding: utf-8 -*-
import pprint

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.tools.safe_eval import json
import logging

_logger = logging.getLogger(__name__)

class ProductTemplateAnalytic(models.Model):
    _name = 'product.template.analytic'

    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account')
    product_template_id = fields.Many2one('product.template', string='Product Template')

    sale_amount = fields.Float(string='Sale Amount')
    sale_qty = fields.Float(string='Sale Quantity')

    customer_bill_amount = fields.Float(string='Customer Amount')
    customer_bill_qty = fields.Float(string='Customer Quantity')

    customer_payment_pending_amount = fields.Float(string='Customer Payment Pending', compute='_compute_payment_pending_amount', store=False, readonly=True)

    purchase_amount = fields.Float(string='Purchase Amount')
    purchase_qty = fields.Float(string='Purchase Quantity')

    vendor_bill_amount = fields.Float(string='Vendor Amount')
    vendor_bill_qty = fields.Float(string='Vendor Quantity')

    vendor_payment_pending_amount = fields.Float(string='Vendor Payment Pending', compute='_compute_payment_pending_amount', store=False, readonly=True)

    def _compute_payment_pending_amount(self):
        for record in self:
            record.customer_payment_pending_amount = 0.0
            record.vendor_payment_pending_amount = 0.0

    def _get_default_values(self):
        return {
            'sale_amount': 0,
            'sale_qty': 0,
            'customer_bill_amount': 0,
            'customer_bill_qty': 0,
            'purchase_amount': 0,
            'purchase_qty': 0,
            'vendor_bill_amount': 0,
            'vendor_bill_qty': 0,
        }

    def _cron_compute_new(self):
        _logger.info("Cron: _cron_compute_new Started")
        self.sudo().search([]).unlink()

        # analitic_account_ids = self.env['account.analytic.account'].search([])
        # product_template_ids = self.env['product.template'].search([])

        sale_order_line_ids = self.env['sale.order.line'].search([])
        customer_move_line_ids = self.env['account.move.line'].search([('move_id.move_type', '=', 'out_invoice')])

        purchase_order_line_ids = self.env['purchase.order.line'].search([])
        vendor_move_line_ids = self.env['account.move.line'].search([('move_id.move_type', '=', 'in_invoice')])

        AAA = self.env['account.analytic.account']
        AAALine = self.env['account.analytic.line']

        data = {}
        # for analitic_account_id in analitic_account_ids:
        for sale_line in sale_order_line_ids:
            # try:
            #     distribution = json.loads(sale_line.x_studio_composition)
            # except:
            #     print(f"No se pudo evaluar {sale_line.x_studio_composition}")
            #     continue
            distribution = sale_line.analytic_distribution
            analitic_account_old_id = sale_line.order_id.analytic_account_id
            if not distribution:
                if not analitic_account_old_id:
                    continue
                else:
                    distribution = {str(analitic_account_old_id.id): 100}

            for account_id in distribution.keys():
                analitic_account_id = AAA.browse(int(account_id))
                to_this_account = distribution[account_id]

                if analitic_account_id.id not in data.keys():
                    data[analitic_account_id.id] = {}
                if sale_line.product_id.product_tmpl_id.id not in data[analitic_account_id.id].keys():
                    data[analitic_account_id.id][sale_line.product_id.product_tmpl_id.id] = self._get_default_values()
                data[analitic_account_id.id][sale_line.product_id.product_tmpl_id.id]['sale_amount'] += sale_line.price_total * (to_this_account / 100)
                data[analitic_account_id.id][sale_line.product_id.product_tmpl_id.id]['sale_qty'] += sale_line.product_uom_qty * (to_this_account / 100)

        for purchase_line in purchase_order_line_ids:
            distribution = purchase_line.analytic_distribution
            if not distribution:
                continue
            for purchase_line_account_line in distribution.keys():
                analitic_account_id = AAA.browse(int(purchase_line_account_line))
                to_this_account = distribution[purchase_line_account_line]

                if analitic_account_id.id not in data.keys():
                    data[analitic_account_id.id] = {}
                if purchase_line.product_id.product_tmpl_id.id not in data[analitic_account_id.id].keys():
                    data[analitic_account_id.id][purchase_line.product_id.product_tmpl_id.id] = self._get_default_values()
                data[analitic_account_id.id][purchase_line.product_id.product_tmpl_id.id]['purchase_amount'] += purchase_line.price_subtotal * (to_this_account / 100)
                data[analitic_account_id.id][purchase_line.product_id.product_tmpl_id.id]['purchase_qty'] += purchase_line.product_qty * (to_this_account / 100)

        for move_line in customer_move_line_ids:
            distribution = move_line.analytic_distribution
            if not distribution:
                continue
            for account_id in distribution.keys():
                analitic_account_id = AAA.browse(int(account_id))
                to_this_account = distribution[account_id]

                if analitic_account_id.id not in data.keys():
                    data[analitic_account_id.id] = {}
                if move_line.product_id.product_tmpl_id.id not in data[analitic_account_id.id].keys():
                    data[analitic_account_id.id][move_line.product_id.product_tmpl_id.id] = self._get_default_values()
                data[analitic_account_id.id][move_line.product_id.product_tmpl_id.id]['customer_bill_amount'] += move_line.price_total * (to_this_account / 100)
                data[analitic_account_id.id][move_line.product_id.product_tmpl_id.id]['customer_bill_qty'] += move_line.quantity * (to_this_account / 100)

        for move_line in vendor_move_line_ids:
            distribution = move_line.analytic_distribution
            if not distribution:
                continue
            for account_id in distribution.keys():
                analitic_account_id = AAA.browse(int(account_id))
                to_this_account = distribution[account_id]

                if analitic_account_id.id not in data.keys():
                    data[analitic_account_id.id] = {}
                if move_line.product_id.product_tmpl_id.id not in data[analitic_account_id.id].keys():
                    data[analitic_account_id.id][move_line.product_id.product_tmpl_id.id] = self._get_default_values()
                data[analitic_account_id.id][move_line.product_id.product_tmpl_id.id]['vendor_bill_amount'] += move_line.price_total * (to_this_account / 100)
                data[analitic_account_id.id][move_line.product_id.product_tmpl_id.id]['vendor_bill_qty'] += move_line.quantity * (to_this_account / 100)


        # pprint.pp(data)
        for acc_id in data:
            for prod_id in data[acc_id]:
                self.create({
                    'analytic_account_id': acc_id,
                    'product_template_id': prod_id,
                    'sale_amount': data[acc_id][prod_id]['sale_amount'],
                    'sale_qty': data[acc_id][prod_id]['sale_qty'],
                    'customer_bill_amount': data[acc_id][prod_id]['customer_bill_amount'],
                    'customer_bill_qty': data[acc_id][prod_id]['customer_bill_qty'],
                    'purchase_amount': data[acc_id][prod_id]['purchase_amount'],
                    'purchase_qty': data[acc_id][prod_id]['purchase_qty'],
                    'vendor_bill_amount': data[acc_id][prod_id]['vendor_bill_amount'],
                    'vendor_bill_qty': data[acc_id][prod_id]['vendor_bill_qty'],
                })

        _logger.info("Cron: _cron_compute_new Finished")


