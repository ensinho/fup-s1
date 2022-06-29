linhas = int(input("Quantas linhas na primeira matriz? "))
colunas = int(input("Quantas colunas na primeira matriz? "))


# função do preenchimento da matriz
def criar_matriz(n, m):
    m1 = []
    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(
                int(input(f"DIgite o elemento[{i}][{j}] da mat{n}x{m} ")))
        m1.append(linha)
    return m1


mat = criar_matriz(linhas, colunas)


# função do cálculo da media da matriz.
def media_matriz(mat):
  # se cria um contador, a partir do 0
    soma = 0
    for i in range(linhas):
        for j in range(colunas):
          # adiciona os elementos somando eles pelo contador
            soma += mat[i][j]
    print(soma)
    # calculo da media em si da matriz
    media = soma/(linhas*colunas)
    return media


# saida de dados com o chamado da função
media_final = media_matriz(mat)
print(media_final)
