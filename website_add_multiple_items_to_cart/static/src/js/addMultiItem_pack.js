odoo.define('website_add_multiple_items_to_cart.addMultiItem', function(require) {
    "use strict";

    // Import required modules
    var ajax = require('web.ajax');
    var publicWidget = require('web.public.widget');

    // Define a public widget to enhance cart functionality
    publicWidget.registry.WebsiteCart = publicWidget.Widget.extend({
        selector: '.o_wsale_products_main_row',

        events: {
            'click #o_add_to_the_pack': '_onClickAddToPack',
        },

        // Event handler for adding multiple items to the cart.
        _onClickAddToPack: function(ev) {
            ev.preventDefault();
            let self = this;
            let productId = ev.currentTarget.getAttribute('data-product-id');

            // Ensure productId is valid before proceeding
            if (!productId || isNaN(productId)) {
                console.error('Invalid product ID:', productId);
                return;
            }

            // Retrieve current cart quantity using AJAX request
            ajax.jsonRpc('/shop/cart/qty', 'call', {}).then(function(qtyCart) {
                sessionStorage.setItem('website_sale_cart_quantity', qtyCart);
                var crtQty = sessionStorage.getItem('website_sale_cart_quantity');
                // Update displayed cart quantity based on retrieved value
                if (crtQty === 'undefined') {
                    self.$el.find('.my_cart_quantity').text(0);
                } else {
                    self.$el.find(".my_cart_quantity").text(qtyCart);
                }

                // Prepare data for adding selected product to cart using AJAX
                $.ajax({
                    type: "get",
                    url: "/shop/cart/add_multi_product",
                    data: {
                        'product_id': productId
                    },
                    success: function(response) {
                        // Update total cart quantity in sessionStorage
                        if ('website_sale_cart_quantity' in sessionStorage) {
                            var currentCartQty = sessionStorage.getItem('website_sale_cart_quantity');
                            sessionStorage.setItem('website_sale_cart_quantity', JSON.stringify(Number(currentCartQty) + 1));
                        }
                        // Optionally, update the UI or redirect to the '/shop' page
                        window.location = '/shop';
                    },
                    error: function() {
                        console.error('Failed to add product to cart.');
                    }
                });
            });
        },
    });
});
