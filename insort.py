####################################
# algoritmo para ordenar una lista #
####################################
A = [5,2,4,6,1,3,1,100,45,2]
# len(A) longitud de la lista
print (A)
for j in range(1,len(A)): #empezamos con el segundo de la lista 
    key = A[j]
    i = j - 1 # vamos a compara con el valor que esta a la 
    while i >-1 and A[i]>key:
        A[i+1] = A[i]
        i = i -1
    A[i+1] = key
print (A)    
    
    
