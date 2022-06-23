# preenchimento de matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Digite o valor da posição [{i}, {j}]: "))
print(matriz)


# funçaoo para criaçao de matriz
def começo(m):
    matriz = [m*[0], m*[0], m*[0], m*[0]]
    for i in range(0, m):
        for j in range(0, m):
            matriz[i][j] = int(input(f"Digite o elemento [{i}, {j}]: "))
    return matriz


# programa principal
m = int(input("Digite a ordem da sua matriz: "))
teste = começo(m)
print(teste)
