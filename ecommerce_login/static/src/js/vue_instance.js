$( document ).ready(function(){

    let divFields = new Vue({
    el: '#divFields',
    data: {
      name: '',
      lastname: '',
      email: '',
      phonenumber: '',
      address1: '',
      address2: '',
      postalcode: '',
      city: '',
      contry: ''
    },
    });
    
   
      var checkbox = document.getElementById("flexCheckDefault");
      var billingAddressContainer = document.getElementById("billingAddressContainer");
      if (checkbox){
        checkbox.addEventListener("change", function() {
          if (this.checked) {
          billingAddressContainer.style.display = "block";
          } else {
          billingAddressContainer.style.display = "none";
          }
        });
      };

      let modal_save = document.getElementById('modal_save');
      let modal_complete = document.querySelector('#modal_dlna_process_complete');
      if (modal_save){
        modal_save.addEventListener('click', (e) => {
          e.preventDefault();
          var el = $('#form-mlnda');
          var data = el.serializeJSON();
          var canvas = document.getElementById('signature-pad');
          var dataURL = canvas.toDataURL();
          $.ajax({
              type: 'POST',
              url: '/web/signup/saveMldna',
              data: { data, 'img': dataURL},
              context: this
          }).done(function(responseText) {
                $('#modal_dlna_process_complete').modal('show');
          });
        })
      }

      let btn_modal_complete = document.querySelector('#btn_close_process_complete');
      if (btn_modal_complete) {
        btn_modal_complete.addEventListener('click', (e) => {
          e.preventDefault();
          $('#modal_lnda').hide();
        });
      }

         

    //firma
    function pointerDown(evt) {
      ctx.beginPath();
      ctx.moveTo(evt.offsetX, evt.offsetY);
      canvas.addEventListener("mousemove", paint, false);
    }

    function pointerUp(evt) {
        canvas.removeEventListener("mousemove", paint);
        paint(evt);
    }

    function paint(evt) {
        ctx.lineTo(evt.offsetX, evt.offsetY);
        ctx.stroke();
    }

  var canvas = document.getElementById("signature-pad");
  if (canvas){
    ctx = canvas.getContext("2d");  
    canvas.addEventListener("mousedown", pointerDown, false);
    canvas.addEventListener("mouseup", pointerUp, false); 
  }

});