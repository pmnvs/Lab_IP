numero, binario = 8, ""  #en este caso le damos cualquier valor a la variable "numero" y estamos inicializando una cadena vacía
if numero == 0:  print("0")  # si el número es es comparado con 0, se imprime 0
while numero > 0: binario, numero = str(numero % 2) + binario, numero // 2 # cuando el número es mayor que 0, se realiza la operación de módulo 2 y división entre 2 entera para convertir el número a binario
print (binario)  #imprimimos la conversión al binario del numero dado 