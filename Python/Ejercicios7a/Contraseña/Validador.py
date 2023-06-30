"""CONTRASENA SEGURA
Crea un script que solicite una contraseña, analice si es segura y si no lo es
sugiera una nueva contraseña. Para ello puedes crear un script validador.py
que contenga una funcion validar_contrasena que reciba una cadena y
verifique si cumple con los requisitos mínimos de una contraseña segura
(por ejemplo, longitud mínima, presencia de letras mayúsculas, letras
minúsculas, números y caracteres especiales). La función debe devolver un
valor booleano que indique si la contraseña es válida o no. Por otro lado
puedes crear otro script creador.py con una función llamada
generar_contrasena que genere contraseñas seguras de forma aleatoria. La
función debe permitir especificar la longitud de la contraseña y qué tipos de
caracteres deben incluirse (por ejemplo, letras mayúsculas, letras
minúsculas, números y caracteres especiales).
(Para el generador de contraseñas puedes probar a usar los modulos
random y string)"""

def validar_contraseña(contrasena):

# Condiciones minimas
    longitud = 8
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_caracter_especial = False

# Comprobamos longitud
    if len(contrasena) < longitud:
        return False

# Caracteres de la contraseña   
    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        else:
            tiene_caracter_especial = True

# Devolvemos True si todas las condiciones se cumplen y False si alguna de ellas no se cumple
    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_caracter_especial

