a = [2,2,5,6]
b = [0,3,7,4]
c = [8,8,5,2]
d = [1,5,6,1]
matrix = [a, b, c, d]

def imprimir(m):
    for i in m:
        print("| ", end="")
        for j in i:
            print (j, end=" ")
        print("|")
    print ("")

print ("Original:")
imprimir(matrix)

print ("Subarray 3:")
print(matrix[2], end="\n\n")        # Sabemos que es el array 3, entonces harcodeamos

print ("Diagonal en cero:")
n=0
for i in matrix:
    print("| ", end="")
    for j in range(0,len(i)):
        if j==n:
            print ("0", end=" ")
        else:
            print (i[j], end=" ")
    print("|")
    n += 1
print ("")

print ("Suma de todos los elementos:", end=" ")
sum=0
for i in matrix:
    for j in i:
        sum += j
print (sum, end = "\n\n")

print ("Seteo de valores Pares en 0, Impares en 1:")
for i in matrix:
    for j in range(0, len(i)):
        if (i[j]%2)==0:
            i[j]=0
        else:
            i[j]=1        
imprimir(matrix)

