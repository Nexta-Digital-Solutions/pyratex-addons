# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Bizople Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details.

# from odoo import models, fields, api

# class ProductPublishedUnPublishedWizard(models.TransientModel):
#     _name = "product.published.unpublished.wizard"
#     _description = "Product Publish Unpublish Wizard"
#
#     website_published = fields.Selection([
#         ("publish", "Publish"), ("unpublish", "Unpublish")], "Website Publish",
#         default="publish")
#     line_ids = fields.One2many(
#         "product.published.lines", "wizard_id", "Wizard Lines")
#
#     @api.model
#     def default_get(self, fields_list):
#         res = super(ProductPublishedUnPublishedWizard, self).default_get(
#             fields_list)
#         active_ids = self.env.context.get("active_ids", [])
#         line_ids = []
#         for product_id in active_ids:
#             product_name = ""
#             product = self.env['product.template'].browse(product_id)
#             if product.default_code:
#                 product_name = "[%s]" % product.default_code
#             if product_name:
#                 product_name = product_name + " " + product.name
#             else:
#                 product_name = product.name
#             line_ids.append([0, False, {
#                 'product_id': product_id,
#                 'product_name': product_name
#             }])
#         res['line_ids'] = line_ids
#         return res
#
#     def get_product_publish_unpublish(self):
#         self.ensure_one()
#         publish = True
#         if self.website_published == 'unpublish':
#             publish = False
#         for line in self.line_ids:
#             line.product_id.website_published = publish
#         return True
#
#
# class ProductPublishedLines(models.TransientModel):
#     _name = "product.published.lines"
#     _description = "Product Published Lines"
#
#     wizard_id = fields.Many2one(
#         'product.published.unpublished.wizard', "Wizard")
#     product_id = fields.Many2one("product.template", "Product")
#     product_name = fields.Char("Product Name")



from odoo import api, fields, models

# class ProductPublishedUnPublishedWizard(models.TransientModel):
#     _name = "product.published.unpublished.wizard"
#     _description = "Product Publish Unpublish Wizard"
#
#     website_published = fields.Selection([
#         ("publish", "Publish"), ("unpublish", "Unpublish")], "Website Publish",
#         default="publish")
#     line_ids = fields.One2many(
#         "product.published.lines", "wizard_id", "Wizard Lines")
#
#     @api.model
#     def default_get(self, fields_list):
#         res = super(ProductPublishedUnPublishedWizard, self).default_get(
#             fields_list)
#         active_ids = self.env.context.get("active_ids", [])
#         line_ids = []
#         for product_id in active_ids:
#             product = self.env['product.product'].browse(product_id)
#             product_name = product.display_name
#             line_ids.append([0, False, {
#                 'product_id': product_id,
#                 'product_name': product_name
#             }])
#         res['line_ids'] = line_ids
#         return res
#
#     def get_product_publish_unpublish(self):
#         self.ensure_one()
#         publish = self.website_published == 'publish'
#         active_id = self._context.get('active_id')
#         line = self.line_ids.filtered(lambda x: x.product_id.id == active_id)
#         if line:
#             line.product_id.website_published = publish
#         return True
#
#
#
#
#
# class ProductPublishedLines(models.TransientModel):
#     _name = "product.published.lines"
#     _description = "Product Published Lines"
#
#     wizard_id = fields.Many2one(
#         'product.published.unpublished.wizard', "Wizard")
#     product_id = fields.Many2one("product.product", "Product Variant")
#     product_name = fields.Char("Product Name")


class ProductPublishedUnPublishedWizard(models.TransientModel):
    _name = "product.published.unpublished.wizard"
    _description = "Product Publish Unpublish Wizard"

    website_published = fields.Selection([
        ("publish", "Publish"), ("unpublish", "Unpublish")], "Website Publish",
        default="publish")
    line_ids = fields.One2many(
        "product.published.lines", "wizard_id", "Wizard Lines")

    def get_product_publish_unpublish(self):
        self.ensure_one()
        publish = self.website_published == 'publish'
        active_id = self._context.get('active_id')
        product = self.env['product.product'].browse(active_id)
        if product:
            product.website_published = publish
        return True


class ProductPublishedLines(models.TransientModel):
    _name = "product.published.lines"
    _description = "Product Published Lines"

    wizard_id = fields.Many2one(
        'product.published.unpublished.wizard', "Wizard")
    product_id = fields.Many2one("product.product", "Product Variant")
    product_name = fields.Char("Product Name")
