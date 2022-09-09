# funcion par calcular los numeros del 1 al n

def suma(n):
    s= 0  #inicializamos la variable
    for x in range (1,n+1):
        s = s + x
    print (s)

n = int(input("Ingrese un numero: "))
suma(n)

