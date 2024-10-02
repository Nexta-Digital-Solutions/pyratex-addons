from odoo import api, fields, models, _, tools
import logging
from odoo.osv import expression
from collections import defaultdict, OrderedDict

_logger = logging.getLogger(__name__)



class ProductProduct(models.Model):
    _inherit = ['product.product', "website.seo.metadata",
                'website.published.multi.mixin',
                'website.searchable.mixin',
                'rating.mixin']

    _name = 'product.product'


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
    def get_open_pack(self, product_name):
        product = self.env.search([('name', '=', product_name)], limit=1)
        if product:
            return product.id
        else:
            return None

    @api.onchange('colorgroup_id')
    def _onchange_colorgroup_id(self):
        for product in self:
            color = product.product_template_attribute_value_ids.filtered(
                lambda template: template.display_type == 'color')
            if color:
                color.product_attribute_value_id.update({'colorgroup_id': product.colorgroup_id.id})

    # def _get_website_ribbon(self):
    #     if self.website_ribbon_id:
    #         return self.website_ribbon_id
    #     return self.product_tag_ids.ribbon_id[:1] or self.product_variant_ids.additional_product_tag_ids.ribbon_id[:1]
    #
    # def _get_suitable_image_size(self, columns, x_size, y_size):
    #     if x_size == 1 and y_size == 1 and columns >= 3:
    #         return 'image_512'
    #     return 'image_1024'
    #
    # def _get_image_holder(self):
    #     """Returns the holder of the image to use as default representation.
    #     If the product template has an image it is the product template,
    #     otherwise if the product has variants it is the first variant
    #
    #     :return: this product template or the first product variant
    #     :rtype: recordset of 'product.template' or recordset of 'product.product'
    #     """
    #     self.ensure_one()
    #     if self.image_128:
    #         return self
    #     variant = self.env['product.product'].browse(self._get_first_possible_variant_id())
    #     # if the variant has no image anyway, spare some queries by using template
    #     return variant if variant.image_variant_128 else self
    #
    # @tools.ormcache('self.id')
    # def _get_first_possible_variant_id(self):
    #     """See `_create_first_product_variant`. This method returns an ID
    #     so it can be cached."""
    #     self.ensure_one()
    #     return self._create_first_product_variant().id
    #
    # def _create_first_product_variant(self, log_warning=False):
    #     """Create if necessary and possible and return the first product
    #     variant for this template.
    #
    #     :param log_warning: whether a warning should be logged on fail
    #     :type log_warning: bool
    #
    #     :return: the first product variant or none
    #     :rtype: recordset of `product.product`
    #     """
    #     return self._create_product_variant(self._get_first_possible_combination(), log_warning)
    #
    # def _create_product_variant(self, combination, log_warning=False):
    #     """ Create if necessary and possible and return the product variant
    #     matching the given combination for this template.
    #
    #     It is possible to create only if the template has dynamic attributes
    #     and the combination itself is possible.
    #     If we are in this case and the variant already exists but it is
    #     archived, it is activated instead of being created again.
    #
    #     :param combination: the combination for which to get or create variant.
    #         The combination must contain all necessary attributes, including
    #         those of type no_variant. Indeed even though those attributes won't
    #         be included in the variant if newly created, they are needed when
    #         checking if the combination is possible.
    #     :type combination: recordset of `product.template.attribute.value`
    #
    #     :param log_warning: whether a warning should be logged on fail
    #     :type log_warning: bool
    #
    #     :return: the product variant matching the combination or none
    #     :rtype: recordset of `product.product`
    #     """
    #     self.ensure_one()
    #
    #     Product = self.env['product.product']
    #
    #     product_variant = self._get_variant_for_combination(combination)
    #     if product_variant:
    #         if not product_variant.active and self.has_dynamic_attributes() and self._is_combination_possible(combination):
    #             product_variant.active = True
    #         return product_variant
    #
    #     if not self.has_dynamic_attributes():
    #         if log_warning:
    #             _logger.warning('The user #%s tried to create a variant for the non-dynamic product %s.' % (self.env.user.id, self.id))
    #         return Product
    #
    #     if not self._is_combination_possible(combination):
    #         if log_warning:
    #             _logger.warning('The user #%s tried to create an invalid variant for the product %s.' % (self.env.user.id, self.id))
    #         return Product
    #
    #     return Product.sudo().create({
    #         'product_tmpl_id': self.id,
    #         'product_template_attribute_value_ids': [(6, 0, combination._without_no_variant_attributes().ids)]
    #     })
    #
    # def _get_first_possible_combination(self, parent_combination=None, necessary_values=None):
    #     """See `_get_possible_combinations` (one iteration).
    #
    #     This method return the same result (empty recordset) if no
    #     combination is possible at all which would be considered a negative
    #     result, or if there are no attribute lines on the template in which
    #     case the "empty combination" is actually a possible combination.
    #     Therefore the result of this method when empty should be tested
    #     with `_is_combination_possible` if it's important to know if the
    #     resulting empty combination is actually possible or not.
    #     """
    #     return next(self._get_possible_combinations(parent_combination, necessary_values), self.env['product.template.attribute.value'])
    #
    # def _get_possible_combinations(self, parent_combination=None, necessary_values=None):
    #     """Generator returning combinations that are possible, following the
    #     sequence of attributes and values.
    #
    #     See `_is_combination_possible` for what is a possible combination.
    #
    #     When encountering an impossible combination, try to change the value
    #     of attributes by starting with the further regarding their sequences.
    #
    #     Ignore attributes that have no values.
    #
    #     :param parent_combination: combination from which `self` is an
    #         optional or accessory product.
    #     :type parent_combination: recordset `product.template.attribute.value`
    #
    #     :param necessary_values: values that must be in the returned combination
    #     :type necessary_values: recordset of `product.template.attribute.value`
    #
    #     :return: the possible combinations
    #     :rtype: generator of recordset of `product.template.attribute.value`
    #     """
    #     self.ensure_one()
    #
    #     if not self.active:
    #         return _("The product template is archived so no combination is possible.")
    #
    #     necessary_values = necessary_values or self.env['product.template.attribute.value']
    #     necessary_attribute_lines = necessary_values.mapped('attribute_line_id')
    #     attribute_lines = self.valid_product_template_attribute_line_ids.filtered(lambda ptal: ptal not in necessary_attribute_lines)
    #
    #     if not attribute_lines and self._is_combination_possible(necessary_values, parent_combination):
    #         yield necessary_values
    #
    #     product_template_attribute_values_per_line = [
    #         ptal.product_template_value_ids._only_active()
    #         for ptal in attribute_lines
    #     ]
    #
    #     for partial_combination in self._cartesian_product(product_template_attribute_values_per_line, parent_combination):
    #         combination = partial_combination + necessary_values
    #         if self._is_combination_possible(combination, parent_combination):
    #             yield combination
    #
    #     return _("There are no remaining possible combination.")
    #
    #
    # def _is_combination_possible(self, combination, parent_combination=None, ignore_no_variant=False):
    #     """
    #     The combination is possible if it is not excluded by any rule
    #     coming from the current template, not excluded by any rule from the
    #     parent_combination (if given), and there should not be any archived
    #     variant with the exact same combination.
    #
    #     If the template does not have any dynamic attribute, the combination
    #     is also not possible if the matching variant has been deleted.
    #
    #     Moreover the attributes of the combination must excatly match the
    #     attributes allowed on the template.
    #
    #     :param combination: the combination to check for possibility
    #     :type combination: recordset `product.template.attribute.value`
    #
    #     :param ignore_no_variant: whether no_variant attributes should be ignored
    #     :type ignore_no_variant: bool
    #
    #     :param parent_combination: combination from which `self` is an
    #         optional or accessory product.
    #     :type parent_combination: recordset `product.template.attribute.value`
    #
    #     :return: whether the combination is possible
    #     :rtype: bool
    #     """
    #     self.ensure_one()
    #
    #     if not self._is_combination_possible_by_config(combination, ignore_no_variant):
    #         return False
    #
    #     variant = self._get_variant_for_combination(combination)
    #
    #     if self.has_dynamic_attributes():
    #         if variant and not variant.active:
    #             # dynamic and the variant has been archived
    #             return False
    #     else:
    #         if not variant or not variant.active:
    #             # not dynamic, the variant has been archived or deleted
    #             return False
    #
    #     parent_exclusions = self._get_parent_attribute_exclusions(parent_combination)
    #     if parent_exclusions:
    #         # parent_exclusion are mapped by ptav but here we don't need to know
    #         # where the exclusion comes from so we loop directly on the dict values
    #         for exclusions_values in parent_exclusions.values():
    #             for exclusion in exclusions_values:
    #                 if exclusion in combination.ids:
    #                     return False
    #
    #     return True
    #
    # def _is_combination_possible_by_config(self, combination, ignore_no_variant=False):
    #     """Return whether the given combination is possible according to the config of attributes on the template
    #
    #     :param combination: the combination to check for possibility
    #     :type combination: recordset `product.template.attribute.value`
    #
    #     :param ignore_no_variant: whether no_variant attributes should be ignored
    #     :type ignore_no_variant: bool
    #
    #     :return: wether the given combination is possible according to the config of attributes on the template
    #     :rtype: bool
    #     """
    #     self.ensure_one()
    #
    #     attribute_lines = self.valid_product_template_attribute_line_ids
    #
    #     if ignore_no_variant:
    #         attribute_lines = attribute_lines._without_no_variant_attributes()
    #
    #     if len(combination) != len(attribute_lines):
    #         # number of attribute values passed is different than the
    #         # configuration of attributes on the template
    #         return False
    #
    #     if attribute_lines != combination.attribute_line_id:
    #         # combination has different attributes than the ones configured on the template
    #         return False
    #
    #     if not (attribute_lines.product_template_value_ids._only_active() >= combination):
    #         # combination has different values than the ones configured on the template
    #         return False
    #
    #     exclusions = self._get_own_attribute_exclusions()
    #     if exclusions:
    #         # exclude if the current value is in an exclusion,
    #         # and the value excluding it is also in the combination
    #         for ptav in combination:
    #             for exclusion in exclusions.get(ptav.id):
    #                 if exclusion in combination.ids:
    #                     return False
    #
    #     return True
    #
    #
    # def _get_own_attribute_exclusions(self):
    #     """Get exclusions coming from the current template.
    #
    #     Dictionnary, each product template attribute value is a key, and for each of them
    #     the value is an array with the other ptav that they exclude (empty if no exclusion).
    #     """
    #     self.ensure_one()
    #     product_template_attribute_values = self.valid_product_template_attribute_line_ids.product_template_value_ids
    #     return {
    #         ptav.id: [
    #             value_id
    #             for filter_line in ptav.exclude_for.filtered(
    #                 lambda filter_line: filter_line.product_tmpl_id == self
    #             ) for value_id in filter_line.value_ids.ids
    #         ]
    #         for ptav in product_template_attribute_values
    #     }
    #
    # def _get_variant_for_combination(self, combination):
    #     """Get the variant matching the combination.
    #
    #     All of the values in combination must be present in the variant, and the
    #     variant should not have more attributes. Ignore the attributes that are
    #     not supposed to create variants.
    #
    #     :param combination: recordset of `product.template.attribute.value`
    #
    #     :return: the variant if found, else empty
    #     :rtype: recordset `product.product`
    #     """
    #     self.ensure_one()
    #     filtered_combination = combination._without_no_variant_attributes()
    #     return self.env['product.product'].browse(self._get_variant_id_for_combination(filtered_combination))
    #
    # @tools.ormcache('self.id', 'frozenset(filtered_combination.ids)')
    # def _get_variant_id_for_combination(self, filtered_combination):
    #     """See `_get_variant_for_combination`. This method returns an ID
    #     so it can be cached.
    #
    #     Use sudo because the same result should be cached for all users.
    #     """
    #     self.ensure_one()
    #     domain = [('product_tmpl_id', '=', self.id)]
    #     combination_indices_ids = filtered_combination._ids2str()
    #
    #     if combination_indices_ids:
    #         domain = expression.AND([domain, [('combination_indices', '=', combination_indices_ids)]])
    #     else:
    #         domain = expression.AND([domain, [('combination_indices', 'in', ['', False])]])
    #
    #     return self.env['product.product'].sudo().with_context(active_test=False).search(domain, order='active DESC',
    #                                                                                      limit=1).id
    #
    # def has_dynamic_attributes(self):
    #     """Return whether this `product.template` has at least one dynamic
    #     attribute.
    #
    #     :return: True if at least one dynamic attribute, False otherwise
    #     :rtype: bool
    #     """
    #     self.ensure_one()
    #     return any(a.create_variant == 'dynamic' for a in self.valid_product_template_attribute_line_ids.attribute_id)
    #
    # def _get_parent_attribute_exclusions(self, parent_combination):
    #     """Get exclusions coming from the parent combination.
    #
    #     Dictionnary, each parent's ptav is a key, and for each of them the value is
    #     an array with the other ptav that are excluded because of the parent.
    #     """
    #     self.ensure_one()
    #     if not parent_combination:
    #         return {}
    #
    #     result = {}
    #     for product_attribute_value in parent_combination:
    #         for filter_line in product_attribute_value.exclude_for.filtered(
    #             lambda filter_line: filter_line.product_tmpl_id == self
    #         ):
    #             # Some exclusions don't have attribute value. This means that the template is not
    #             # compatible with the parent combination. If such an exclusion is found, it means that all
    #             # attribute values are excluded.
    #             if filter_line.value_ids:
    #                 result[product_attribute_value.id] = filter_line.value_ids.ids
    #             else:
    #                 result[product_attribute_value.id] = filter_line.product_tmpl_id.mapped('attribute_line_ids.product_template_value_ids').ids
    #
    #     return result
    #
    #
    # def _cartesian_product(self, product_template_attribute_values_per_line, parent_combination):
    #     """
    #     Generate all possible combination for attributes values (aka cartesian product).
    #     It is equivalent to itertools.product except it skips invalid partial combinations before they are complete.
    #
    #     Imagine the cartesian product of 'A', 'CD' and range(1_000_000) and let's say that 'A' and 'C' are incompatible.
    #     If you use itertools.product or any normal cartesian product, you'll need to filter out of the final result
    #     the 1_000_000 combinations that start with 'A' and 'C' . Instead, This implementation will test if 'A' and 'C' are
    #     compatible before even considering range(1_000_000), skip it and and continue with combinations that start
    #     with 'A' and 'D'.
    #
    #     It's necessary for performance reason because filtering out invalid combinations from standard Cartesian product
    #     can be extremely slow
    #
    #     :param product_template_attribute_values_per_line: the values we want all the possibles combinations of.
    #     One list of values by attribute line
    #     :return: a generator of product template attribute value
    #     """
    #     if not product_template_attribute_values_per_line:
    #         return
    #
    #     all_exclusions = {self.env['product.template.attribute.value'].browse(k):
    #                       self.env['product.template.attribute.value'].browse(v) for k, v in
    #                       self._get_own_attribute_exclusions().items()}
    #     # The following dict uses product template attribute values as keys
    #     # 0 means the value is acceptable, greater than 0 means it's rejected, it cannot be negative
    #     # Bear in mind that several values can reject the same value and the latter can only be included in the
    #     #  considered combination if no value rejects it.
    #     # This dictionary counts how many times each value is rejected.
    #     # Each time a value is included in the considered combination, the values it rejects are incremented
    #     # When a value is discarded from the considered combination, the values it rejects are decremented
    #     current_exclusions = defaultdict(int)
    #     for exclusion in self._get_parent_attribute_exclusions(parent_combination):
    #         current_exclusions[self.env['product.template.attribute.value'].browse(exclusion)] += 1
    #     partial_combination = self.env['product.template.attribute.value']
    #
    #     # The following list reflects product_template_attribute_values_per_line
    #     # For each line, instead of a list of values, it contains the index of the selected value
    #     # -1 means no value has been picked for the line in the current (partial) combination
    #     value_index_per_line = [-1] * len(product_template_attribute_values_per_line)
    #     # determines which line line we're working on
    #     line_index = 0
    #
    #     while True:
    #         current_line_values = product_template_attribute_values_per_line[line_index]
    #         current_ptav_index = value_index_per_line[line_index]
    #         current_ptav = current_line_values[current_ptav_index]
    #
    #         # removing exclusions from current_ptav as we're removing it from partial_combination
    #         if current_ptav_index >= 0:
    #             for ptav_to_include_back in all_exclusions[current_ptav]:
    #                 current_exclusions[ptav_to_include_back] -= 1
    #             partial_combination -= current_ptav
    #
    #         if current_ptav_index < len(current_line_values) - 1:
    #             # go to next value of current line
    #             value_index_per_line[line_index] += 1
    #             current_line_values = product_template_attribute_values_per_line[line_index]
    #             current_ptav_index = value_index_per_line[line_index]
    #             current_ptav = current_line_values[current_ptav_index]
    #         elif line_index != 0:
    #             # reset current line, and then go to previous line
    #             value_index_per_line[line_index] = - 1
    #             line_index -= 1
    #             continue
    #         else:
    #             # we're done if we must reset first line
    #             break
    #
    #         # adding exclusions from current_ptav as we're incorporating it in partial_combination
    #         for ptav_to_exclude in all_exclusions[current_ptav]:
    #             current_exclusions[ptav_to_exclude] += 1
    #         partial_combination += current_ptav
    #
    #         # test if included values excludes current value or if current value exclude included values
    #         if current_exclusions[current_ptav] or \
    #                 any(intersection in partial_combination for intersection in all_exclusions[current_ptav]):
    #             continue
    #
    #         if line_index == len(product_template_attribute_values_per_line) - 1:
    #             # submit combination if we're on the last line
    #             yield partial_combination
    #         else:
    #             # else we go to the next line
    #             line_index += 1
    # def _search_get_detail(self, website, order, options):
    #     with_image = options['displayImage']
    #     with_description = options['displayDescription']
    #     with_category = options['displayExtraLink']
    #     with_price = options['displayDetail']
    #     domains = [website.sale_product_domain()]
    #     category = options.get('category')
    #     min_price = options.get('min_price')
    #     max_price = options.get('max_price')
    #     attrib_values = options.get('attrib_values')
    #     fiberfamily = options.get('fiberfamily')
    #     # colorgroup = options.get('colorgroup')
    #     structure = options.get('structure')
    #     property = options.get('property')
    #     usage = options.get('usage')
    #     availablemeters = options.get('availablemeters')
    #     producttype = options.get('producttype')
    #     careinstructions = options.get('careinstructions')
    #     certification = options.get('certification')
    #
    #     if category:
    #         domains.append([('public_categ_ids', 'child_of', unslug(category)[1])])
    #     if min_price:
    #         domains.append([('list_price', '>=', min_price)])
    #     if max_price:
    #         domains.append([('list_price', '<=', max_price)])
    #     if fiberfamily:
    #         domains.append([('fiberfamily_id', '=', int(fiberfamily))])
    #     # if colorgroup:
    #     #     domains.append([('product_variant_ids.colorgroup_id', '=', int(colorgroup))])
    #     if structure:
    #         domains.append([('structure_id', '=', int(structure))])
    #     if property:
    #         domains.append([('property_id', '=', int(property))])
    #     if usage:
    #         domains.append([('usage_id', '=', int(usage))])
    #     if availablemeters:
    #         domains.append([('id', 'in', availablemeters)])
    #     if producttype:
    #         domains.append([('producttype_id', '=', int(producttype))])
    #     if careinstructions:
    #         domains.append([('careinstructions_id', '=', int(careinstructions))])
    #     if certification:
    #         domains.append([('certification_id', '=', int(certification))])
    #     if attrib_values:
    #         attrib = None
    #         ids = []
    #         for value in attrib_values:
    #             if not attrib:
    #                 attrib = value[0]
    #                 ids.append(value[1])
    #             elif value[0] == attrib:
    #                 ids.append(value[1])
    #             else:
    #                 domains.append([('attribute_line_ids.value_ids', 'in', ids)])
    #                 attrib = value[0]
    #                 ids = [value[1]]
    #         if attrib:
    #             domains.append([('attribute_line_ids.value_ids', 'in', ids)])
    #     search_fields = ['name', 'product_variant_ids.default_code']
    #     fetch_fields = ['id', 'name', 'website_url']
    #     mapping = {
    #         'name': {'name': 'name', 'type': 'text', 'match': True},
    #         'product_variant_ids.default_code': {'name': 'product_variant_ids.default_code', 'type': 'text',
    #                                              'match': True},
    #         'website_url': {'name': 'website_url', 'type': 'text', 'truncate': False},
    #     }
    #     if with_image:
    #         mapping['image_url'] = {'name': 'image_url', 'type': 'html'}
    #     if with_description:
    #         # Internal note is not part of the rendering.
    #         search_fields.append('description')
    #         fetch_fields.append('description')
    #         search_fields.append('description_sale')
    #         fetch_fields.append('description_sale')
    #         mapping['description'] = {'name': 'description_sale', 'type': 'text', 'match': True}
    #     if with_price:
    #         mapping['detail'] = {'name': 'price', 'type': 'html', 'display_currency': options['display_currency']}
    #         mapping['detail_strike'] = {'name': 'list_price', 'type': 'html',
    #                                     'display_currency': options['display_currency']}
    #     if with_category:
    #         mapping['extra_link'] = {'name': 'category', 'type': 'html'}
    #     return {
    #         'model': 'product.product',
    #         'base_domain': domains,
    #         'search_fields': search_fields,
    #         'fetch_fields': fetch_fields,
    #         'mapping': mapping,
    #         'icon': 'fa-shopping-cart',
    #     }
