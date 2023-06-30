import random
import string

def generar_contrasena_segura(longitud, incluir_minuscula = True, incluir_mayuscula = True, incluir_digitos = True, incluir_caracyer_especial = True):

    caracteres = ""
    if incluir_mayuscula:
        caracteres += string.ascii_uppercase 
    
    if incluir_minuscula:
        caracteres += string.ascii_lowercase 

    if incluir_digitos:
        caracteres += string.digits
    
    if incluir_caracyer_especial:
        caracteres += string.punctuation

    contrasena = "".join(random.choice(caracteres) for i in range(longitud))

    return contrasena
