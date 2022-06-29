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


# função do percorrimento até o maior elemento
def maior_elemento(mat):
  # fixa o maior elemento como o primeiro, para ir testando ao longo da matriz
    maior = mat[0][0]
    for i in range(linhas):
        for j in range(colunas):
          # testa se o primeiro elemento é maior ou igual, para atribuí-lo à esse valor
            if maior <= mat[i][j]:
                maior = mat[i][j]
                # fixando suas posições, como pedido na questão
                maior_linha = i
                maior_coluna = j
    return maior, maior_linha, maior_coluna


# função do percorrimento até o menor elemento
def menor_elemento(mat):
    menor = mat[0][0]
    for i in range(linhas):
        for j in range(colunas):
          # testa se o primeiro elemento é menor ou igual, para atribuí-lo à esse valor
            if mat[i][j] <= menor:
                menor = mat[i][j]
                # novamente fixando suas posições
                menor_linha = i
                menor_coluna = j
    return menor, menor_linha, menor_coluna


# saida de dados com o chamado das funções criadas
mat = criar_matriz(linhas, colunas)

# atribuindo estes novos valores com os valores retornados pela função
elemento_maior, linha_maior, coluna_maior = maior_elemento(mat)
elemento_menor, linha_menor, coluna_menor = menor_elemento(mat)

# formatação na saida dos dados
print(
    f"O maior elemento é: [{elemento_maior}] na posição [{linha_maior}][{coluna_maior}] ")
print(
    f"O menor elemento é: [{elemento_menor}] na posição [{linha_menor}][{coluna_menor}] ")
