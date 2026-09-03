operador = input("Ingrese el operador (+, -, *, /): ")
O1= input("Ingrese el primer operador: ")
O2= input("Ingrese el segundo operador: ")
resultado = O1 + operador + O2
resultado = eval(str(O1) + operador + str(O2))
print ("El resultado de la operación es: ", resultado)

