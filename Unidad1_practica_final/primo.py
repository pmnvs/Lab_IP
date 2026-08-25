n =int(input("Ingrese un número:"))
if n <= 1:
    print ("El número no es primo") 
i= 2
while i <= n:
    if n == 2:
        print("El número es primo")
        break
    if n%i == 0:
        print("El número no es primo")
        break
    elif n%i == 0 and i== n:
        print("El número es primo")
        break
    elif n%i != 0 and i< n:
        print("El número es primo")
        break
    i += 1
