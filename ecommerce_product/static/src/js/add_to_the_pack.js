odoo.define('ecommerce_product.add_to_the_pack', function (require) {
    "use strict";

    // const selectedProductIds = [];
    //
    // $(document).on('click', '#o_add_to_the_pack', function () {
    //     const productId = $(this).data('product-id');
    //     console.log('Product ID:', productId);
    //     addToThePack(productId);
    // });
    //
    // function addToThePack(productId) {
    //     // Agregar el ID del producto seleccionado a la lista de IDs
    //     selectedProductIds.push(productId);
    //     console.log('Selected Product IDs:', selectedProductIds);
    //
    //     // Mostrar los IDs de los productos seleccionados en la pantalla
    //     const idsElement = $('#wrap').prev().find('p');
    //     idsElement.text('Selected Product IDs: ' + selectedProductIds.join(', '));
    // }


    const selectedProductIds = [];

    $(document).on('click', '#o_add_to_the_pack', function (evt) {
        const productId = $(this).data('product-id');
        console.log('Product ID:', productId);
        console.log(evt);
        addToThePack(productId);
    });

    function addToThePack(productId) {
        selectedProductIds.push(productId);
        console.log('Selected Array Product IDs:', selectedProductIds);

        const idsElement = $('#allProducts p[name="productsArray"]');
        // idsElement.attr('name', 'productsArray').text(selectedProductIds.join(', '));
        idsElement.attr('name', 'productsArray').text(selectedProductIds);
    }

});