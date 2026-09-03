for numero in range(2, 101): 
    if numero%numero == 0 and numero%1 == 0 and numero%2 != 0 and numero%3 != 0 and numero%5 != 0 and numero%7 != 0:
        print(numero)