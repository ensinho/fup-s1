a  = [0]*10
b = [0]*10
c = [0]*10
for i in range(10):
    a[i] = int(input("Digite o %d termo: " %(i+1)))
contp = 0 
conti = 0
j = 0
k = 0
for i in range(10):
    if a[i]%2 == 0:
        b[j] = a[i]
        j = j + 1
        contp += 1
    else:
        c[k] = a[i]
        k = k + 1
        conti += 1
print('%d de pares ' %contp)
for i in range(contp):
    print(b[i])
print('%d de impares ' %conti)
for i in range(conti):
    print(c[i])


        

