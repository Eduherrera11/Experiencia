print("Bienvenido al programa")
name = input("Ingrese su correo electronico: ")

usuario = "eduardoaugusto.eh@gmail.com"
clave = "Eduherrera1"

if name.lower() == usuario:
   contraseña = input("Ingrese su contraseña: ") 
   if contraseña.title() == clave:
      print("Bienvenido has iniciado correctamente")
   else:
        if contraseña != clave:
            contraseña = input("La contraseña es incorrecta vuelve a intentarlo: ")
            if contraseña == clave:
                print("Bienvenido has iniciado correctamente")
            else:
                contraseña = input("La contraseña es incorrecta vuelve a intentarlo: ")
                if contraseña == clave:
                    print("Bienvenido has iniciado correctamente")
                else:
                    print("La contrasena es incorrecta, el programa ha finalizado")   
else:
    print("El usuario o la contraseña han sido incorrectos, el programa ha finalizado")      


    

