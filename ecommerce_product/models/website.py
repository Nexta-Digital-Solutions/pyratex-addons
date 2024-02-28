
class WebsitePublishedMultiMixin(WebsitePublishedMixin):

    _name = 'website.published.multi.mixin'
    _inherit = ['website.published.mixin', 'website.multi.mixin']
    _description = 'Multi Website Published Mixin'

    # website_published = fields.Boolean(compute='_compute_website_published',
    #                                    inverse='_inverse_website_published',
    #                                    search='_search_website_published',
    #                                    related=False, readonly=False)
    website_published = fields.Boolean()