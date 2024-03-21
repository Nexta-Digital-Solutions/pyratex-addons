
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
//                 $('#packPrice').text(selectedPack.price + '€').css('color', 'blue').css('font-size', '25px');
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
//                 method: 'get_results',
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

    $(document).ready(async function() {
        const packs = await getOpenPacks();
        const smallPack = packs.find(pack => pack.name === "Small");
        if (smallPack) {
            $('select[name="openpack"]').val(smallPack.id).change();
        }
    });

    $(document).on('change', 'select[name="openpack"]', async function () {
        const selectedId = $(this).val();
        console.log(selectedId);
        if (selectedId) {
            const packs = await getOpenPacks();
            const selectedPack = packs.find(pack => pack.id === parseInt(selectedId));
            if (selectedPack) {
                $('#packPrice').text(selectedPack.price + '€').css('color', 'blue').css('font-size', '25px');
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


