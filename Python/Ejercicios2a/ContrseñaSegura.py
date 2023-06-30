clave = input("ingrese una contraseña: ")

if ("a" in clave or "e" in clave or "i" in clave or "o" in clave or "u" in clave) and ("*" in clave or "#" in clave):
    print("Clave es verdadero")
else:
    print("Clave es falso")