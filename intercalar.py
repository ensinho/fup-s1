l1 = []
l2 = [] 

while True:
    n = int(input("DIgite um elemento: "))
    if n >0:
        l1.append(n)
    if n < 0 or n > 10: 
        print("DEixa de ser zé lesado ")
        break

while True:
    m = int(input("DIgite outro elemento: "))
    if m  >0:
        l2.append(m)
    if m < 0 or n > 10: 
        print("DEixa de ser zé lesado ")
        break
l4 = []
l4.append(l1)
l4.append(l2)

l3 = []

for i in l1:
    l3.append(i)
for x in l2:
    l3.insert(1,x)

print(l3)

'''i = 0
pos = 0
tam1 = len(primeira_lista)
tam2 = len(segunda_lista)
lista_inter = []
while i < tam1:
    lista_inter.append(primeira_lista[i])
    lista_inter.append(segunda_lista[i])
    i = i + 1
    pos = i

for i in range(pos, tam2):
    lista_inter.append(segunda_lista[i])
print(lista_inter)'''