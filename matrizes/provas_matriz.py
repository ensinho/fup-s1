# Faça um programa que preencha uma matriz 6 × 3 com as notas de seis
# alunos em três provas. O programa deverá mostrar um relatório com o
# número dos alunos (número da linha) e a prova em que cada aluno obteve
# menor nota. Ao final do relatório, deverá mostrar quantos alunos tiveram
# menor nota em cada uma das provas: na prova 1, na prova 2 e na prova 3.

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


def menor_nota(notas):
    menor_nota = notas[0][0]
    for i in range(linhas):
        for j in range(colunas):
            if menor_nota <= notas[0][j]:
                menor_nota = notas[0][j]
                lin_menor = i
                col_menor = j
            menor_nota = 0
        print(
            f"A menor nota do aluno[{lin_menor}][{col_menor}] foi: {menor_nota}")
        menor_nota = 0


notas = criar_matriz(linhas, colunas)
nota_menor = menor_nota(notas)
