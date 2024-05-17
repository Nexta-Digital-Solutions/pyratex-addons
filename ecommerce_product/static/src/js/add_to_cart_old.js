odoo.define('ecommerce_product.add_to_cart', function (require) {
    "use strict";

    const addToThePackModule = require('ecommerce_product.add_to_the_pack');
    const productId = $(this).data('product-id');
    let cart = []; // Array para representar el carrito de compras

//    async function addToCart(productId) {
//        cart.push(productId);
//    }

    async function addAllToCart() {
        const selectedProductIds = addToThePackModule.getSelectedProductIds();
        for (const productId of selectedProductIds) {
            await addToCart(productId);
        }
        console.log('Todos los productos del pack han sido añadidos al carrito.');
    }

    $(document).on('click', '#o_add_to_Cart', async function () {
        await addAllToCart();
        alert('Todos los productos del pack han sido añadidos al carrito.');
    });
});

//odoo.define('ecommerce_product.add_to_cart', function (require) {
//    "use strict";
//    const rpc = require('web.rpc');
//
//    const getSelectedProductIds = require('ecommerce_product.add_to_the_pack').getSelectedProductIds;


//        async function getIdFromProductProduct() {
//        let result;
//
//        await rpc.query({
//            model: 'product.template',
//            method: 'search_read',
//			args: [[ [$(this).data('product-id')] ], ['lst_price'] ]
//        }).then(function (data) {
//            console.log('Data', data);
//            result = data});
//        return result;
//        };

//GUILLE
//    async function setPackPrice(id, price) {
//        console.log('Setting pack price. ID:', id, 'Price:', price);
//        const result = await rpc.query({
//            model: 'product.product',
//            method: 'write',
//            args: [[id], {lst_price: parseFloat(price)}]
//        });
//        console.log('Set pack price result:', result);
//        return result;
//    }

//GUILLE
//        async function addToProductPack(packId, templateIds) {
//        await rpc.query({
//            model: 'product.pack.line',
//            method: 'search_read',
//            args: [
//                [['parent_product_id', '=', packId]],
//                ['id'],
//            ],
//        }).then(async (existingLines) => {
//            if (existingLines.length > 0) {
//                await rpc.query({
//                    model: 'product.pack.line',
//                    method: 'unlink',
//                    args: [existingLines.map(line => line.id)],
//                });
//            }
//        });
//
//        const templateCounts = {};
//        templateIds.forEach(templateId => {
//            templateCounts[templateId] = (templateCounts[templateId] || 0) + 1;
//        });
//
//        const promises = Object.entries(templateCounts).map(async ([templateId, quantity]) => {
//            const productIdsData = await rpc.query({
//                model: 'product.product',
//                method: 'search_read',
//                args: [
//                    [['product_tmpl_id', '=', parseInt(templateId)]],
//                    ['id'],
//                ],
//            });
//
//            const productIds = productIdsData.map(productData => productData.id);
//
//            const productPromises = productIds.map(async (productId) => {
//                await rpc.query({
//                    model: 'product.pack.line',
//                    method: 'create',
//                    args: [{
//                        "parent_product_id": packId,
//                        "product_id": productId,
//                        "quantity": quantity
//                    }]
//                });
//            });
//
//            await Promise.all(productPromises);
//        });
//
//        await Promise.all(promises);
//    }

//GUILLE
//    $(document).on('click', '#o_add_to_Cart', async function () {
//        const selectedProductIds = getSelectedProductIds();
//        console.log('Received Product IDs:', selectedProductIds);
//
//        console.log('Received Product IDs:', selectedProductIds);
//        try {
//            const packPrice = window.selectedPackPrice;
//            const resultId = await getIdFromProductProduct();
//
//            await setPackPrice(resultId[0].id, packPrice);
//            await addToProductPack(resultId[0].id, selectedProductIds);
//            console.log('Products added to product pack.');
//        } catch (error) {
//            console.error('Error adding products to product pack:', error);
//        }
//    });
});