# preenchimento de matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f"Digite o valor da posição [{i}, {j}]: "))
print(matriz)
