matriz = []
for i in range(5):
    linha = []
    linha.append(input(f"Digite o nome: "))
    for j in range(1):
        linha.append(int(input(f"Digite a idade [{i}, {j}]: ")))
    matriz.append(linha)
print(matriz)


maioridade = matriz[0][1]
for i in range(5):
    if matriz[i][1] > maioridade:
        maioridade = matriz[i][1]
        nome = matriz[i][0]
print(nome)
print(maioridade)
        