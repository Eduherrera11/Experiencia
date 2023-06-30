'''Supongamos que eres un administrador de sistemas y necesitas validar el acceso de los usuarios 
a un sitio web. Crea un script que verifique si el nombre de usuario y la contraseña ingresados son 
correctos y permita el acceso solo si ambos son correctos. 
Pista 1: Puedes crear dos listas, una con los nombre de usuario como por ejemplo…
nombres_usuario = ["juan123", "ana456", „pedro789"] 
Y otra lista con las contraseñas guardadas para cada usuario… 
contraseñas = ["clave123", "clave456", „clave789"] 
Otra opción puede ser que crees una lista de listas con la forma: 
nombres_contraseñas = [ ["juan123“,"clave123"] , ["ana456“,“clave456“] , ["pedro789“, 
"clave789“] ] 
Despues puedes pedir el usuario y contraseña y comprobar si coinciden. 
Pista 2: Para verificar si el usuario y contraseña son correctos puedes crear un bucle donde 
recorras los nombres de usuario y compruebes con un if si el nombre de usuario introducido y la 
contraseña coinciden con los datos de tus listas.'''

nombres_usuarios = ["juan123", "ana456", "pedro789"]
passwords = ["clave123", "clave456", "clave789"]

print("Bienvenido al programa")

usuario = str(input("Ingrese el usuario: "))
password = str(input("Ingrese la clave: "))

credenciales = False
for i in range(len(nombres_usuarios)):
    if nombres_usuarios[i] == usuario and passwords[i] == password:
     credenciales = True

if credenciales == True:
    print("Acceso permitido")
else:
    print("Acceso denegado")