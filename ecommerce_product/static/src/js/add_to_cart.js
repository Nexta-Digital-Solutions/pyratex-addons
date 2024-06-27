//from sweetalert2 import Swal;
//import swal from 'swal';

odoo.define('ecommerce_product.add_to_cart', function (require) {
    "use strict";
    const rpc = require('web.rpc');
    const ajax = require('web.ajax');
    var wSaleUtils = require('website_sale.utils');

    const getSelectedProductIds = require('ecommerce_product.add_to_the_pack').getSelectedProductIds;


        async function getIdFromProductName(ProductName) {
        let result;

        await rpc.query({
            model: 'product.product',
            method: 'search_read',
			args: [[ ['name','=', ProductName]], ['id'] ]
        }).then(function (data) {
            console.log('Data', data);
            result = data});
        return result;
        };

        async function getIdFromProducTemplateId(productId) {
            let result;
    
            await rpc.query({
                model: 'product.product',
                method: 'search_read',
                args: [[ ['product_tmpl_id','=', productId]], ['id', 'list_price'] ]
            }).then(function (data) {
                data[0].list_price = 0;
                result = data});
            return result;
            };


    async function setPackPrice(id, price) {
        console.log('Setting pack price. ID:', id, 'Price:', price);
        const result = await rpc.query({
            model: 'product.template',
            method: 'write',
            args: [[id], {list_price: parseFloat(price)}]
        });
        console.log('Set pack price result:', result);
        return result;
    }

    // Esta funcion es para el pack abierto
    $(document).on('click', '#o_add_to_Cart', async function () {
        let product_ids = []
        const selectedProductIds = getSelectedProductIds();
        
        for (const record of selectedProductIds){
            const product_id = await getIdFromProducTemplateId(record);
            product_ids.push(product_id[0]);
        }
        console.log('Received Product IDs:', selectedProductIds);


        try {
            const packPrice = window.selectedPackPrice;
            const resultIdOpenPack = await getIdFromProductName('Customized Swatchpack');
            resultIdOpenPack[0].list_price = packPrice;

            const productsOpenPack = [ resultIdOpenPack[0] ].concat(product_ids);
            for (const record of productsOpenPack){
                await AddProductOpenPackToCart (record.id, 1, record.list_price, this);
            }
            console.log('Products added to product pack.');
        } catch (error) {

             Swal.fire({
                icon: 'error',
                title: 'Swatchpack',
                text: 'You can only order one Swatch Pack for each order. If you need a larger size, please remove the previous Swatchpack from the shopping cart before adding a new pack',
//                footer: '<a href>Why do I have this issue?</a>'
            });
            console.error('Ops... Error adding products to product pack:', error);
        }
    

    })

    async function AddProductOpenPackToCart (product_id, qty, price_unit, ev) {

        const data = await rpc.query({ 
            route: "/shop/cart/update_json",
            params: {
                product_id: product_id,
                add_qty: qty,
                price_unit: price_unit
            }
        });

        const $navButton = $('header .o_wsale_my_cart').first();
        const imgContainer = $('#products_grid')
        wSaleUtils.animateClone($navButton, imgContainer, 25, 40);
        wSaleUtils.updateCartNavBar(data);  
        
    }
});