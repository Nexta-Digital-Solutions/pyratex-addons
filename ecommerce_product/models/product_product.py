from odoo import api, fields, models, _


class ProductProduct(models.Model):
    _inherit = 'product.product'

    colorgroup_id = fields.Many2one('color.group', string='Color Groups', readonly=False)

    # colorgroup_id = fields.Many2one('product.attribute.value', string='Color Groups', readonly=False, domain="[('attribute_id.name', '=', 'Color')]",)
    # colorgroup_id = fields.Many2one('color.group', string='Color Groups', readonly=False, domain="[('product_attribute_valued_ids.attribute_id.name', '=', 'Color')]", relate="product_attribute_valued_ids.colorgroup_id")

    # colorgroup_id = fields.Many2one('color.group', string='Color Groups', compute='_compute_colorgroup_ids',
    #                                    readonly=False)
    #
    # @api.depends('product_template_variant_value_ids')
    # def _compute_colorgroup_ids(self):
    #     for template in self:
    #         color_groups = template.mapped('product_template_variant_value_ids.product_attribute_value_id.colorgroup_id')
    #         if color_groups:
    #             template.colorgroup_id = color_groups[0]
    #         else:
    #             template.colorgroup_id = False
    @api.onchange('colorgroup_id')
    def _onchange_colorgroup_id(self):
        for product in self:
            color = product.product_template_attribute_value_ids.filtered(lambda template: template.display_type == 'color')
            if color:
                color.product_attribute_value_id.update({'colorgroup_id': product.colorgroup_id.id})


    def _get_website_ribbon(self):
        if self.website_ribbon_id:
            return self.website_ribbon_id
        return self.product_tag_ids.ribbon_id[:1] or self.product_variant_ids.additional_product_tag_ids.ribbon_id[:1]

    def _get_suitable_image_size(self, columns, x_size, y_size):
        if x_size == 1 and y_size == 1 and columns >= 3:
            return 'image_512'
        return 'image_1024'

    def _get_image_holder(self):
        """Returns the holder of the image to use as default representation.
        If the product template has an image it is the product template,
        otherwise if the product has variants it is the first variant

        :return: this product template or the first product variant
        :rtype: recordset of 'product.template' or recordset of 'product.product'
        """
        self.ensure_one()
        if self.image_128:
            return self
        variant = self.env['product.product'].browse(self._get_first_possible_variant_id())
        # if the variant has no image anyway, spare some queries by using template
        return variant if variant.image_variant_128 else self