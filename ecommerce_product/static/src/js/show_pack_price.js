//
// odoo.define('ecommerce_product.show_pack_price', function (require) {
//     "use strict";
//
//     const rpc = require('web.rpc');
//
//     $(document).on('change', 'select[name="openpack"]', async function () {
//         const selectedId = $(this).val();
//         console.log(selectedId);
//         if (selectedId) {
//             const packs = await getOpenPacks();
//             const selectedPack = packs.find(pack => pack.id === parseInt(selectedId));
//             if (selectedPack) {
//                 $('#packPrice').text(selectedPack.price + '€').css('color', 'blue');
//             } else {
//                 $('#packPrice').text('Pack not found');
//             }
//         } else {
//             $('#packPrice').text('');
//         }
//     });
//
//     async function getOpenPacks() {
//         try {
//             const result = await rpc.query({
//                 model: 'open.pack',
//                 method: 'read',
//             });
//             console.log(result);
//             return result;
//         } catch (error) {
//             console.error('Error open packs:', error);
//             return [];
//         }
//     }
// });



odoo.define('ecommerce_product.show_pack_price', function (require) {
    "use strict";

    const rpc = require('web.rpc');

    $(document).on('change', 'select[name="openpack"]', async function () {
        const selectedId = $(this).val();
        console.log(selectedId);
        if (selectedId) {
            const packs = await getOpenPacks();
            const selectedPack = packs.find(pack => pack.id === parseInt(selectedId));
            if (selectedPack) {
                $('#packPrice').text(selectedPack.price + '€').css('color', 'blue');
            } else {
                $('#packPrice').text('Pack not found');
            }
        } else {
            $('#packPrice').text('');
        }
    });

    async function getOpenPacks() {
        try {
            const result = await rpc.query({
                model: 'open.pack',
                method: 'get_results',
            });
            console.log(result);
            return result;
        } catch (error) {
            console.error('Error open packs:', error);
            return [];
        }
    }
});


