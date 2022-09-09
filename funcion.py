# funcion par calcular los numeros del 1 al n

def suma(n):
    s= 0  #inicializamos la variable
    for x in range (1,n+1):
        s = s + x
    print (s)
def suma2(n):
    return n*(n+1)/2


n = int(input("Ingrese un numero: "))
print ("primer metodo")
suma(n)
print ("segundo metodo")
print(suma2(n))


