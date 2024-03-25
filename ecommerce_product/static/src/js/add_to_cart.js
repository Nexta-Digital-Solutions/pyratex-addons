odoo.define('ecommerce_product.add_to_cart', function (require) {
    "use strict";
    const rpc = require('web.rpc');

    const getSelectedProductIds = require('ecommerce_product.add_to_the_pack').getSelectedProductIds;

    // async function addToProductPack(packId, productIds) {
    //     const promises = productIds.map(async (id) => {
    //         await rpc.query({
    //             model: 'product.pack.line',
    //             method: 'create',
    //             args: [{
    //                 // "pack_id": packId,
    //                 "parent_product_id": packId,
    //                 "product_id": id,
    //                 "quantity": 1
    //             }]
    //         });
    //     });
    //     await Promise.all(promises);
    // }

    async function addToProductPack(packId, productIds) {
        const promises = productIds.map(async (id) => {
            // Verificar si ya existe una línea de paquete con el mismo pack_id y product_id
            const existingLine = await rpc.query({
                model: 'product.pack.line',
                method: 'search_read',
                args: [
                    [['parent_product_id', '=', packId], ['product_id', '=', id]],
                    ['id'], // Solo necesitamos el id para verificar si existe
                ],
            });

            // Si no existe la línea de paquete, la creamos
            if (existingLine.length === 0) {
                await rpc.query({
                    model: 'product.pack.line',
                    method: 'create',
                    args: [{
                        "parent_product_id": packId,
                        "product_id": id,
                        "quantity": 1
                    }]
                });
            }
        });

        await Promise.all(promises);
    }


    $(document).on('click', '#o_add_to_Cart', async function () {
        const selectedProductIds = getSelectedProductIds();
        console.log('Received Product IDs:', selectedProductIds);

        try {
            await addToProductPack(66, selectedProductIds); // el id debe ser de la tabla product.product
            console.log('Products added to product pack.');
        } catch (error) {
            console.error('Error adding products to product pack:', error);
        }
    });
});

