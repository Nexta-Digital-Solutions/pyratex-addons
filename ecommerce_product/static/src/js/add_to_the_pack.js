odoo.define('ecommerce_product.add_to_the_pack', function (require) {
    "use strict";

    let selectedProductIds = [];
    let packElementsNumber = 0;

    $(document).on('click', '#o_add_to_the_pack', async function (event) {
        event.preventDefault(); // Evitar el envío del formulario
        const productId = $(this).data('product-id');
        console.log('Product ID:', productId);

        if (packElementsNumber < await getMaxPackElementsNumber()) {
            await addToThePack(productId);
        } else {
            console.log('Cannot add more products to the pack.');
        }
    });

    $(document).on('click', '.remove-from-pack', function (evt) {
        const productIdToRemove = $(this).data('product-id');
        removeProductFromPack(productIdToRemove);
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
        displayProductImage(imageUrl, productId);


        packElementsNumber++;
//        console.log('Suma', packElementsNumber);
    }

    function removeProductFromPack(productIdToRemove) {
        const indexToRemove = selectedProductIds.indexOf(productIdToRemove);
        if (indexToRemove !== -1) {
            selectedProductIds.splice(indexToRemove, 1);
            packElementsNumber--;
            $(`#product_${productIdToRemove}`).remove();
        }
    }

    function displayProductImage(imageUrl, productId) {
        const container = $('#allProducts');
        const imgElement = $('<img>').attr('src', "data:image/jpg;base64," + imageUrl).css({
            'width': '100px',
            'height': '100px'
        });
        imgElement.addClass('img-openpack');
        const removeButton = $('<button>').addClass('remove-from-pack').html('&#10006;').attr('data-product-id', productId).css({
            'position': 'absolute',
            'top': '5px',
            'right': '5px',
            'z-index': '1'
        });
        const divWrapper = $('<div>').attr('id', `product_${productId}`).css({
            'position': 'relative',
            'display': 'inline-block',
            'margin-right': '10px',
            'width': '100px',
            'height': '100px',
            'overflow': 'hidden'
        });
        divWrapper.append(removeButton).append(imgElement);
        container.append(divWrapper);
    }


    async function getMaxPackElementsNumber() {
        const selectedOpenPackId = $('select[name="openpack"]').val();
        if (selectedOpenPackId) {
            const rpc = require('web.rpc');
            const result = await rpc.query({
                model: 'open.pack',
                method: 'read',
                args: [[parseInt(selectedOpenPackId)], ['elements_number']],
            });
            console.log('Cantidad máxima', result[0].elements_number);
            return result[0].elements_number;
        } else {
            return 0;
        }
    }

    $(document).on('change', 'select[name="openpack"]', async function () {
        packElementsNumber = 0;
        selectedProductIds = [];
    });

     function getSelectedProductIds() {
        return selectedProductIds;
    }

    return {
        getSelectedProductIds: getSelectedProductIds,
        addToThePack: addToThePack
    };
});

