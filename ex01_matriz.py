#funçao preencher matriz
def começo(m):
    matriz = []
    for i in range(m):
        linha = []
        for j in range(m):
            linha.append(int(input(f"Digite o elemento [{i}, {j}]: ")))
        matriz.append(linha)
    return matriz
    print(matriz)


m = int(input("Digite a ordem da sua matriz: "))
teste = começo(m)
print(teste)

n = int(input("Digite a ordem da sua matriz: "))
teste2 = começo(n)
print(teste2)


for i in range(m):
    for j in range(n):
        mult = (teste2[j][i] * teste[i][j])

for j in range(m):
    for i in range(n):
        mult2 = (teste2[i][j] * teste[i][j])

#funçao conferir 
resultante = []
for i in range(m):
    linhar = []
    for j in range(m):
        linhar.append(mult)
        linhar.append(mult2)
    resultante.append(linhar)
print(resultante)


