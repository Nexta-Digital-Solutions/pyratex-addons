from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    country_id = fields.Many2one('res.country', string='Made in')
    width = fields.Float(string='Width', digits = (4,2))
    description_ecommerce = fields.Text(string='Ecommerce Sales Description')
    fiberfamily_id = fields.Many2one('fiber.family', string='Fiber Family')
    property_id = fields.Many2many('properties', string='Property')
    usage_id = fields.Many2many('usage', string='Usage')
    producttype_id = fields.Many2one('product.type', string='Product Type')
    structure_id = fields.Many2one('structure', string='Structure')
    careinstructions_id = fields.Many2many('care.instructions', string='Care Instructions')
    certification_id = fields.Many2many('certification', string='Certification')
    composition_id = fields.Many2many('composition', string='Composition')

    def _get_combination_info(self, combination=False, product_id=False, add_qty=1, pricelist=False, parent_combination=False, only_template=False):
        """Override for website, where we want to:
            - take the website pricelist if no pricelist is set
            - apply the b2b/b2c setting to the result

        This will work when adding website_id to the context, which is done
        automatically when called from routes with website=True.
        """
        self.ensure_one()

        current_website = False

        if self.env.context.get('website_id'):
            current_website = self.env['website'].get_current_website()
            if not pricelist:
                pricelist = current_website.get_current_pricelist()

        combination_info = super(ProductTemplate, self)._get_combination_info(
            combination=combination, product_id=product_id, add_qty=add_qty, pricelist=pricelist,
            parent_combination=parent_combination, only_template=only_template)

        product = self.env['product.product'].sudo().browse(combination_info['product_id']) or self
        qty_available = product.qty_available or 0
        
        combination_info.update( qty_available=qty_available )
        
        """
        if self.env.context.get('website_id'):
            partner = self.env.user.partner_id
            company_id = current_website.company_id
            fpos_id = self.env['website'].sudo()._get_current_fiscal_position_id(partner)
            fiscal_position = self.env['account.fiscal.position'].sudo().browse(fpos_id)
            product_taxes = product.sudo().taxes_id.filtered(lambda x: x.company_id == company_id)
            taxes = fiscal_position.map_tax(product_taxes)

            price = self._price_with_tax_computed(
                combination_info['price'], product_taxes, taxes, company_id, pricelist, product,
                partner
            )
            if pricelist.discount_policy == 'without_discount':
                list_price = self._price_with_tax_computed(
                    combination_info['list_price'], product_taxes, taxes, company_id, pricelist,
                    product, partner
                )
            else:
                list_price = price
            price_extra = self._price_with_tax_computed(
                combination_info['price_extra'], product_taxes, taxes, company_id, pricelist,
                product, partner
            )
            has_discounted_price = pricelist.currency_id.compare_amounts(list_price, price) == 1
            prevent_zero_price_sale = not price and current_website.prevent_zero_price_sale

            compare_list_price = self.compare_list_price
            if pricelist and pricelist.currency_id != product.currency_id:
                compare_list_price = self.currency_id._convert(self.compare_list_price, pricelist.currency_id, self.env.company,
                                                  fields.Datetime.now(), round=False)

            combination_info.update(
                base_unit_name=product.base_unit_name,
                base_unit_price=product._get_base_unit_price(list_price),
                price=price,
                list_price=list_price,
                qty_available=qty_available,
                price_extra=price_extra,
                has_discounted_price=has_discounted_price,
                prevent_zero_price_sale=prevent_zero_price_sale,
                compare_list_price=compare_list_price
            )
        """
        return combination_info