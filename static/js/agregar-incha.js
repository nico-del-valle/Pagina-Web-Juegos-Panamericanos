const validateEmail = (email) => {
    if (!email) return false;
    // length validation
    let lengthValid = email.length > 15;

    // format validation
    let re = /^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z.]{2,}$/;  // explicar en el README, los email que aceptan
    let formatValid = re.test(email);

    //return logic AND of validations.
    return lengthValid && formatValid;
};

const validatePhoneNumber = (phoneNumber) => {
    if (!phoneNumber) return true;
    // length validation
    let lengthValid = phoneNumber.length >= 12;
  
    // format validation
    let re = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/;
    let formatValid = re.test(phoneNumber);
  
    // return logic AND of validations.
    return lengthValid && formatValid;
};

const validateName = (nombre) => {
    if (!nombre) return false;
    // length validation
    let lengthValid = nombre.length >= 3 && nombre.length <= 80;
    // no double spaces (or more) validation
    if (nombre.includes("  ")) return false;
    // format validation
    let re = /^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+ [a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$/;
    let formatValid = re.test(nombre);

    return lengthValid && formatValid;
};

const validateFiles = (files) => {
    if (!files) return false;
  
    // number of files validation
    let lengthValid = 1 <= files.length && files.length <= 3;
  
    // file type validation
    let typeValid = true;
  
    for (const file of files) {
      // file.type should be "image/<foo>" or "application/pdf"
      let fileFamily = file.type.split("/")[0];
      typeValid &&= fileFamily == "image" || file.type == "application/pdf";
    }
  
    // return logic AND of validations.
    return lengthValid && typeValid;
};

const validateComent = (coment) => {
    
    let re = /^[a-zA-Z0-9 ]*$/;  // explicar en el README, los que se acepta
    let formatValid = re.test(coment);


    // Devuelve la lógica AND de las validaciones.
    return formatValid;
};

const validateOption = (option) => {
    if (!option)  return false;
    // length validation

    let lengthValid = (option.length >= 1 && option.length <= 3);
 

    return lengthValid;
    
};





const validateForm = () => {
    let myForm = document.forms["hincha-form"];
    let nombre = myForm["nombre"].value;
    let email = myForm["email"].value;
    let phoneNumber = myForm["numero"].value;
    let coment = myForm["comentario"].value;
    let deportesSelect = document.getElementById("deportes"); 
    let selectedOptions = Array.from(deportesSelect.selectedOptions);
    let option = selectedOptions.map(option => option.value);
    let region = myForm['region'];
    let comuna = myForm['comuna'];
    let transporte = myForm['transporte'];
    

    
    // validation auxiliary variables and function.
    let invalidInputs = [];
    let isValid = true;
    const setInvalidInput = (inputName) => {
        invalidInputs.push(inputName);
        isValid &&= false;
    };

    // validation logic
    if (!validateName(nombre)) {
        setInvalidInput("Nombre")
    }
    
    if (!validateEmail(email)) {
        setInvalidInput("Email");
    }

    if (region.selectedIndex === 0) {
        setInvalidInput('Debes escoger una region');
    }
    if (comuna.selectedIndex === 0) {
        setInvalidInput('Debes escoger una comuna');
    }

    if (transporte.selectedIndex === 0) {
        setInvalidInput('Debes escoger un Modo de transporte');
    }
    
    if (!validatePhoneNumber(phoneNumber)) {
        setInvalidInput("Numero de Contacto");
    }
    
    if (!validateOption(option)) {
        setInvalidInput('Debes escoger de 1 a 3 deportes');
    }
        
    if (!validateComent(coment)) {
        setInvalidInput("Comentarios adicionales");
    }
    
   

    // finally display validation
    let errorModal = document.getElementById("error-modal");
    let validationMessageElem = document.getElementById("val-msg");
    let validationListElem = document.getElementById("val-list");

    if (!isValid) {
        validationListElem.textContent = "";
        // add invalid elements to val-list element.
        for (input of invalidInputs) {
          let listElement = document.createElement("li");
          listElement.innerText = input;
          validationListElem.append(listElement);
        }
        // set val-msg
        validationMessageElem.innerText = "Los siguiente campos son invalidos:";
    
        // make validation prompt visible

        errorModal.style.display = "flex";
        return ;
        
      } else {
        // Ocultar el botón "Registrar Hincha"
        const registrarHinchaBtn = document.getElementById("registrar-hincha");
        registrarHinchaBtn.style.display = "none";
        
        // Mostrar el mensaje de confirmación
        const confirmacionModal = document.getElementById("confirmacion-modal");
        confirmacionModal.style.display = "flex";
        }
};


let RegistrarBtn = document.getElementById("registrar-hincha");
RegistrarBtn.addEventListener("click", validateForm);

const cancelarEnvioBtn = document.getElementById("cancelar-envio-btn");
cancelarEnvioBtn.addEventListener("click", () => {
    // Ocultar el mensaje de confirmación y mostrar el botón "Registrar Hincha"
    const confirmacionModal = document.getElementById("confirmacion-modal");
    confirmacionModal.style.display = "none";
    const registrarArtesanoBtn = document.getElementById("registrar-hincha");
    registrarArtesanoBtn.style.display = "block";
});


// Event listener para el botón "Cerrar" en el mensaje de error de validación
let cerrarErrorBtn = document.getElementById("cerrar-error-btn");
cerrarErrorBtn.addEventListener("click", () => {
// Ocultar el mensaje de error de validación
    const errorModal = document.getElementById("error-modal");
    errorModal.style.display = "none";

});

// Event listener para el botón "Enviar Formulario" en el mensaje de confirmación
const enviarFormularioBtn = document.getElementById("enviar-formulario-btn");
enviarFormularioBtn.addEventListener("click", () => {
    // Enviar el formulario
    const myForm = document.forms["hincha-form"];
    myForm.submit();
});









