$(function(){
    $("#miFormulario").validate({
        rules:{
            txtNombre:{
                required:true,
                minlength:5
            },
            txtPrecio:{
                required:true
            },
            txtUrl:{
                required:true
            }
        },
    })

})