'''1. Define una función llamada "saludar" que tome un parámetro "nombre"
y muestre un saludo personalizado.
2. Crea una función llamada "suma" que tome dos parámetros "a" y "b" e
imprima la suma de ambos.
3. Escribe una función llamada "calcular_area_rectangulo" que tome dos
parámetros "base" y "altura" y calcule el área de un rectángulo.
4. Define una función llamada "imprimir_lista" que tome una lista como
parámetro y la imprima en la consola.
5. Crea una función llamada "es_par" que tome un número como
parámetro e imprima True si es par, o False si es impar.
6. Escribe una función llamada "concatenar_strings" que tome dos
parámetros "cadena1" y “cadena2" e imprima la concatenación de
ambas cadenas.
7. Define una función llamada "obtener_maximo" que tome una lista de
números como parámetro y devuelva el número máximo de la lista.
8. Crea una función llamada "convertir_fahrenheit_a_celsius" que tome un
parámetro "fahrenheit" y devuelva su equivalente en grados Celsius.
9. Escribe una función llamada "calcular_edad" que tome dos parámetros:
"año_actual" y "año_nacimiento" y calcule la edad de una persona.
10. Define una función llamada "es_divisible" que tome dos parámetros
"num" y "divisor" e imprima True si "num" es divisible por "divisor", o
False si no lo es.
11. Crea una función llamada "mostrar_info_persona" que tome tres
argumentos de palabra clave: "nombre", "edad" y "ciudad". La función
debe imprimir en la consola la información de una persona en un
formato legible.
12. Escribe una función llamada "calcular_promedio" que tome una lista de
números como parámetro y calcule el promedio de esos números. Si no
se proporciona una lista, debe usar una lista vacía por defecto.
13. Crea una función llamada "calcular_potencia" que tome dos
parámetros "base" y "exponente", y calcule la potencia de la base
elevada al exponente. Utiliza 2 como valor por defecto para el
exponente.
14. Define una función llamada "imprimir_info_alumno" que tome un
argumento posicional “nombre”(y sin valor por defecto) y varios
argumentos de palabra clave: "edad", "curso" y “promedio" (puedes
ponerles como valor por defecto None). La función debe imprimir la
información del alumno en un formato legible.'''

def saludar_usuario(nombre="carlos"):
    "Funcion para enviar un saludo personalizado"

    print(f"Hola {nombre.title()} es un placer conocerte!")

saludar_usuario("Eduardo")

print("================================")

def suma(num1, num2):
    "Funcion para sumar un parametro a con uno b"

    suma = num1 + num2
    print(f"La suma de los parametros es {suma}")

suma(150, 70)

print("=================================")

def calcula_area_rectangulo(base, altura):
    "Funcion para calcular el area de un rectangulo"

    area = base*altura
    print(f"La base del rectangulo es {base} la altura {altura} por lo tanto el area es {area}")

calcula_area_rectangulo(10, 20)

print("=================================")

def imprimir_lista(lista=["Bugatti", "Lamborgini", "McLaren", "Audi"]):
    "Funcion para imprimir lista"

    print(lista)

imprimir_lista()

print("=================================")

def es_par(num):
    "Funcion para verificar si el parametro es par"

    if num % 2 == 0:
        print(True)
    else:
        print(False)

es_par(10)

print("==================================")

def concatenar_string(cadena1, cadena2):
    "funcion para concatenar dos strings"

    concatenar = cadena1 + cadena2
    print(concatenar)

concatenar_string("Para", "metro")

print("==================================")

def obtener_maximo(lista):
    "Funcion para obtener el max numero de una lista"

    maximo = max(lista)
    print(f"El numero maximo de la lista {lista} es {maximo}")

obtener_maximo(lista=[10, 200, 180, 150])

print("==================================")


def convertir_farenheik_a_celcius(farengeik):
    "Funcion para convertir un parametro de grados farengeik a celcius"

    celcius = (farengeik - 32)*(5/9)
    print(f"Los grados {farengeik} farengeik son {celcius} en celcius")

convertir_farenheik_a_celcius(100)

print("==================================")


def calcular_edad(año_actual, año_nacimiento):
    "Funcion para calcular edad con dos parametros"

    edad = año_actual - año_nacimiento
    print(f"La edad de la persona es {edad}")

calcular_edad(2023, 2003)

print("==================================")

def es_divisible(num, divisor):
    "Funcion para ver si un numero es divisible por otro"

    if num % divisor == 0:
        print(True)
    else:
        print(False)

es_divisible(7, 2)

print("==================================")

def info_persona(nombre, edad, ciudad):
    "Funcion que muestra la info de una persona"

    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")

info_persona("Eduardo", 19, "Dubai")

print("==================================")

def calcular_promedio(lista=[]):
    'Funcion para calcular el promedio de un parametro'

    longitud = len(lista)
    suma = sum(lista)
    promedio = suma/longitud

    print(f"El promedio de la lista {lista} es {promedio}")

calcular_promedio([100, 200, 300])

print("=================================")

def calcular_potencia(exponente, base=2):
    "Funcion para calcular la potencia con dos parametros"

    resultado = base**exponente
    print(f"El resultado de {base} elevado a {exponente} es {resultado}")

calcular_potencia(10)

print("=================================")

def info_alumno(nombre, edad = None, curso = None, promedio = None):
    "Funcion que muestra la info de una persona"

    print(f"Nombre de estudiante: {nombre}")
    if edad is not None:
        print(f"Edad: {edad}")
    if curso is not None:
        print(f"Curso: {curso}")
    if promedio is not None:
        print(f"Promedio: {promedio}")

info_alumno("Eduardo", 19, "USA", 20)

