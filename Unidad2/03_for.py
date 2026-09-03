for numero in range(0,7):  #for es una estructura de control que permite repetir un bloque de código un número determinado de veces, en este caso, desde 0 hasta 6 (7 no incluido)
    cuadrado = numero ** 2
    print(numero, cuadrado)  

materias = ["Python", "Linux", "Interfaces"]  
for posicion, materia in enumerate(materias, start=1):
    print(f"{posicion}. {materia}")

for materia in materias:
    print(materia)
cadena = "0123456789ABCDEF"
for letra in cadena:
    print(letra)

for i in range(len(cadena)):
    print(cadena[i]) 

for numero in range(0,7,2):  
    cuadrado = numero ** 2
    print(numero, cuadrado)