# criação da matriz
matriz = [0][0]

# preenchimento da matriz
for i in range(1, 4):
    for j in range(1, 3):
        valor = input("Digite o elemento matriz[ %d ][ %d ]" % (i, j))
        matriz[i][j] = valor.split()
        print(valor)


# print(matriz[1][1])
'''maior = matriz[1][1]
pos_i = 1
pos_j = 1

for i in range(1, 4):
    for j in range(1, 3):

        if matriz[i][j] > maior:
            maior = matriz[i][j]
            pos_i = i
            pos_j = j

print("O maior elemento da matriz é: ", (matriz[pos_i][pos_j]))
print("E está na linha ", pos_i, "e coluna ", pos_j)'''
