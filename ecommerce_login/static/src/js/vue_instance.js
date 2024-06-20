$( document ).ready(function(){

    let divFields = new Vue({
    el: '#divFields',
    data: {
      name: '',
      lastname: '',
      email: '',
      phonenumber: ''
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
  ctx = canvas.getContext("2d");  
  canvas.addEventListener("mousedown", pointerDown, false);
  canvas.addEventListener("mouseup", pointerUp, false); 

});