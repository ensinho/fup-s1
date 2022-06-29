# Recebimento da ordem da matriz.
lin_m1 = int(input("Quantas linhas na primeira matriz? "))
col_m1 = int(input("Quantas colunas na primeira matriz? "))

# a função para preencher a matriz com a ordem recebida.


def criar_matriz(n, m):
    m1 = []
    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(
                int(input('Digite o elemento mat1[%d][%d] ' % (i, j))))
        m1.append(linha)
    return m1


mat1 = criar_matriz(lin_m1, col_m1)
print(mat1)


def calc_linha(mat, linha, coluna):
    maior = 0
    soma = 0
    mlinha = 0
    for i in range(linha):
        for j in range(coluna):
          # somando todos os termos ao quadrado, como pedido na questão.
            soma += mat[i][j]**2
        if maior <= soma:
          # rodando o contador para zerar sempre que passar de uma linha, porém armazenando esse.
            maior = soma
        soma = 0
    return maior, mlinha


def calc_coluna(mat, lin_m1, col_m1):
    maior = 0
    soma = 0
    mcoluna = 0
    for j in range(col_m1):
        for i in range(lin_m1):
          # girando o contador e conferindo se é menor ou maior, novamente zerando e armazenando.
            soma += mat[i][j]
        if maior <= soma:
            mcoluna = j
            maior = soma
        soma = 0
    return maior, mcoluna


# saida dos dados, chamando as respectivas funções
valor_linha, maior_linha = calc_linha(mat1, lin_m1, col_m1)
valor_coluna, maior_coluna = calc_coluna(mat1, lin_m1, col_m1)

print(f"A linha de maior valor é [{maior_linha}] e valor [{valor_linha}]")

print(f"A coluna de maior valor é [{maior_coluna}] e valor [{valor_coluna}]")
