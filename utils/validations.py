import re 
import filetype
from db import db

# validaciones que sirven para ambos

def validate_nombre(value):
    # vemos que el nombre no sea vacio
    if (value == None):
        return False
    # vemos que el nombre no sea muy largo
    lengthValid = len(value) >= 3 and len(value) <= 80
    # vemos que no tenga espacios seguidos
    if "  " in value:
        return False
    # vemos que el nombre siga el formato requerido
    formatValid = re.match(r"^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+ [a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ,.'-]+$", value)
    return lengthValid and formatValid
    
def validate_email(value):
    # vemos que el email no sea vacio
    if (value == None):
        return False
    # vemos que el email sea del largo correcto
    lengthValid = len(value) > 15
    # revisar que implica esta expresion regular
    validFormat = re.match(r"^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z.]{2,}$", value)
    return lengthValid and validFormat

def validate_number(value):
    # numero puede ser vacio
    if (value == None or value == ""):
        return True
    lengthValid = len(value) >= 12
    # expresion regular para numero de telefono (sin contar el codigo de pais)
    validFormat = re.match(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", value)
    return lengthValid and validFormat

def validate_region(value):
    if (value == None or value == ""):
        return False
    elif(value not in db.get_lista_region()):
        return False

    return True

def validate_comuna_by_region(region, comuna):
    comunas = [comuna_in_lista[0] for comuna_in_lista  in db.get_lista_comunas_by_region(region)]
    if (comuna == None or comuna == ""):
        return False

    elif(comuna not in comunas):
        return False
    
    return True


# validaciones de artesano
def validate_file(files):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png"}

    if len(files) < 1 or len(files) > 3:
        return False
    
    for file in files:
        # check if a file was submitted
        if file is None:
            return False
        
        # check if the browser submitted an empty file
        if file.filename == "":
            return False
        
        # check file extension (falta importa filetype)
        ftype_guess = filetype.guess(file)
        if ftype_guess.extension not in ALLOWED_EXTENSIONS: 
            return False
        #check mimetype
        if ftype_guess.mime not in ALLOWED_MIMETYPES:
            return False
    
    return True

def validate_description(value):
    # puede ser vacio
    if (value == None):
        return True
    validFormat = re.match(r"^[a-zA-Z0-9 ]*$", value)
    return validFormat

def validate_option(tipos):
    if not(1 <= len(tipos) <= 3):
        print("El largo es: ",len(tipos))
        return False
    for tipo in tipos:
        if (tipo not in db.get_tipo_artesania()):
            print("El tipo es: ",tipo)
            print("La lista es :",db.get_tipo_artesania())
            return False
    return True

def validate_artesano(nombre, email, numero, fotos, descripcion,options,region,comuna):
    error = ""
    if not validate_nombre(nombre):
        error += "El nombre no es válido."
    if not validate_email(email):
        error += "El correo electrónico no es válido."
    if not validate_number(numero):
        error += "El número de teléfono no es válido."
    if not validate_description(descripcion):
        error += "La descripción no es válida."
    if not validate_option(options):
        error += "Debes seleccionar de 1 a 3 tipos de artesanía validas."
    if not validate_file(fotos):
        error += "Los archivos adjuntos no son válidos."
    if not validate_region(region):
        error += "La región no es válida."
    if not validate_comuna_by_region(region, comuna):
        error += "La comuna coincide con con la region."
    
    if error == "":
        return True,error
    else:
        return False, error
    

# validaciones de hincha

def validate_comment(comentario):
    # puede ser vacio
    if (comentario == None):
        return True
    
    validLength = len(comentario) <= 80
    validFormat = re.match(r"^[a-zA-Z0-9 ]*$", comentario)
    return validFormat and validLength

def validate_deportes(deportes):
    if not(1 <= len(deportes) <= 3):
        return False
    for deporte in deportes:
        if deporte not in db.get_lista_deportes():
            return False
    return True
    
def validate_transport(transporte):
    opciones = ['locomoción pública','particular']
    if (transporte not in opciones):
        return False
    return True
    
def validate_hincha(nombre, email, numero, comentario, deportes, transporte,region,comuna):
    error = ""
    if not validate_nombre(nombre):
        error += "El nombre no es válido."
    if not validate_email(email):
        error += "El correo electrónico no es válido."
    if not validate_number(numero):
        error += "El número de teléfono no es válido."
    if not validate_region(region):
        error += "La región no es válida."
    if not validate_comuna_by_region(region,comuna):
        error += "La comuna no coincide con la region."
    if not validate_comment(comentario):
        error += "El comentario no es válido."
    if not validate_deportes(deportes):
        error += "Debes seleccionar de 1 a 3 deportes."
    if not validate_transport(transporte):
        error += "El transporte no es válido."

    if error == "":
        return True, error
    else:
        return False, error


    