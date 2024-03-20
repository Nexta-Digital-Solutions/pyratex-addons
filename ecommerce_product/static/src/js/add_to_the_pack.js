// odoo.define('ecommerce_product.add_to_the_pack', function (require) {
//     "use strict";
//
//     // const selectedProductIds = [];
//     //
//     // $(document).on('click', '#o_add_to_the_pack', function () {
//     //     const productId = $(this).data('product-id');
//     //     console.log('Product ID:', productId);
//     //     addToThePack(productId);
//     // });
//     //
//     // function addToThePack(productId) {
//     //     // Agregar el ID del producto seleccionado a la lista de IDs
//     //     selectedProductIds.push(productId);
//     //     console.log('Selected Product IDs:', selectedProductIds);
//     //
//     //     // Mostrar los IDs de los productos seleccionados en la pantalla
//     //     const idsElement = $('#wrap').prev().find('p');
//     //     idsElement.text('Selected Product IDs: ' + selectedProductIds.join(', '));
//     // }
//
//
//     const selectedProductIds = [];
//
//     $(document).on('click', '#o_add_to_the_pack', function (evt) {
//         const productId = $(this).data('product-id');
//         console.log('Product ID:', productId);
//         console.log(evt);
//         addToThePack(productId);
//     });
//
//     function addToThePack(productId) {
//         selectedProductIds.push(productId);
//         console.log('Selected Array Product IDs:', selectedProductIds);
//
//         const idsElement = $('#allProducts p[name="productsArray"]');
//         // idsElement.attr('name', 'productsArray').text(selectedProductIds.join(', '));
//         idsElement.attr('name', 'productsArray').text(selectedProductIds);
//     }
//
// });



odoo.define('ecommerce_product.add_to_the_pack', function (require) {
    "use strict";

    const selectedProductIds = [];

    $(document).on('click', '#o_add_to_the_pack', async function (evt) {
        const productId = $(this).data('product-id');
        console.log('Product ID:', productId);
        // console.log(evt);
        await addToThePack(productId);
    });

    async function addToThePack(productId) {
        selectedProductIds.push(productId);
        console.log('Selected Array Product IDs:', selectedProductIds);

        const rpc = require('web.rpc');
        const result = await rpc.query({
            model: 'product.template',
            method: 'read',
            args: [[productId], ['image_1920']],
        });
        const imageUrl = result[0].image_1920;
        displayProductImage(imageUrl);
    }

    function displayProductImage(imageUrl) {
        const container = $('#allProducts');
        // añadiendo data:image/jpg;base64, transforma la imagen de base 64 a jpg
        const imgElement = $('<img>').attr('src', "data:image/jpg;base64," + imageUrl).css({'width': '50px', 'height': '50px'});
        container.append(imgElement);
    }
});
