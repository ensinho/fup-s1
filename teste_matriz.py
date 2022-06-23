matriz = [[0, 0, 0,0], [0, 0,0, 0]]
for i in range(2):
    for j in range(4):
        matriz[i][j] = int(input(f"Digite o valor da posição [{i}, {j}]: "))
print(matriz)