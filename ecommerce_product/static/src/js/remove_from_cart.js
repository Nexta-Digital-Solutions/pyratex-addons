odoo.define('ecommerce_product.remove_from_cart', function (require) {
    'use strict';

    var core = require('web.core');
    var publicWidget = require('web.public.widget');

    publicWidget.registry.WebsiteSale.include({
        _onClickDeleteProduct: function (ev) {
            ev.preventDefault();
            var $row = $(ev.currentTarget).closest('tr');
            var productName = $row.find('.td-product_name').text().trim();

            if (productName === 'Customized Swatchpack') {
                $row.find('.js_quantity').val(0).trigger('change');
            }
        },
    });
});
