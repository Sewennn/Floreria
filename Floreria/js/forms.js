document.getElementById("valNombre").style.display = "none";
document.getElementById("valApellido").style.display = "none";
document.getElementById("valTelefono").style.display = "none";
document.getElementById("valRut").style.display = "none";
document.getElementById("valEmail").style.display = "none";

function validarFormulario(){
    let nombre = document.getElementById("floatingInputName").value;
    let apellido = document.getElementById("floatingInputLName").value;
    let telefono = document.getElementById("floatingInputPhone").value;
    let rut = document.getElementById("floatingInputRut").value;
    
    if (nombre.length == 0) {
        document.getElementById("valNombre").style.display = "inline";
        document.getElementById("floatingInputName").classList.add("is-invalid");
    }else{
        document.getElementById("valNombre").style.display = "none";
        document.getElementById("floatingInputName").classList.remove("is-invalid");
        document.getElementById("floatingInputName").classList.add("is-valid");
    }
    if (apellido.length == 0) {
        document.getElementById("valApellido").style.display = "inline";
        document.getElementById("floatingInputLName").classList.add("is-invalid");
    }else{
        document.getElementById("valApellido").style.display = "none";
        document.getElementById("floatingInputLName").classList.remove("is-invalid");
        document.getElementById("floatingInputLName").classList.add("is-valid");
    }
    if (telefono.length != 9 ) {
        document.getElementById("valTelefono").style.display = "inline";
        document.getElementById("floatingInputPhone").classList.add("is-invalid");
    }else{
        document.getElementById("valTelefono").style.display = "none";
        document.getElementById("floatingInputPhone").classList.remove("is-invalid");
        document.getElementById("floatingInputPhone").classList.add("is-valid");
    }
    if (rut.length >= 11 || rut.length <= 8 ) {
        document.getElementById("valRut").style.display = "inline";
        document.getElementById("floatingInputRut").classList.add("is-invalid");
    }else{
        document.getElementById("valRut").style.display = "none";
        document.getElementById("floatingInputRut").classList.remove("is-invalid");
        document.getElementById("floatingInputRut").classList.add("is-valid");
    }
}

function validateEmail(){
	var emailField = document.getElementById("floatingInputEmail");
	var validEmail =  /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;
	if( validEmail.test(emailField.value) ){
        document.getElementById("valEmail").style.display = "none";
        document.getElementById("floatingInputEmail").classList.add("is-valid");
	}else{
        document.getElementById("valEmail").style.display = "inline";
        document.getElementById("floatingInputEmail").classList.add("is-invalid");
        document.getElementById("floatingInputEmail").classList.remove("is-valid");
	}
} 

document.getElementById("ocultar").style.display = "none";

function pass(){
    let input = document.getElementById("txtPassword");
    if (input.type == "password") {
        input.type = "text";
        document.getElementById("ocultar").style.display = "inline";
        document.getElementById("mostrar").style.display = "none";
    }else{
        input.type = "password";
        document.getElementById("ocultar").style.display = "none";
        document.getElementById("mostrar").style.display = "inline";
    }
}
