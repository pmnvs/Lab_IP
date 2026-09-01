numero, octal=8, ""  #en este caso le damos cualquier valor a la variable "numero" y estamos inicializando una cadena vacía
if numero == 0:  print ("0")  # si el número es es comparado con 0, se imprime 0
while numero > 0: octal, numero = str(numero % 8) + octal, numero // 8  # cuando el número es mayor que 0, se realiza la operación de módulo 8 y división entre 8 entera para convertir el número a octal
print (octal)  #imprimimos la conversión al octal del numero dado