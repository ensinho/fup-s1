l_mat1 = int(input('Digite a qtde de linhas da matriz 1: '))
c_mat1 = int(input('Digite a qtde de coluna da matriz 1: '))

l_mat2 = int(input('Digite a qtde de linhas da matriz 2: '))
c_mat2 = int(input('Digite a qtde de colunas da matriz 1: '))

mat1 = []
for i in range(l_mat1):
  linha = []
  for j in range(c_mat1):
    linha.append(int(input('Digite o elemento mat1[%d][%d] ' %(i,j))))
  mat1.append(linha)
print("A primeira matriz é: ", mat1)

mat2 = []
for i in range(l_mat2):
  linha = []
  for j in range(c_mat2):
    linha.append(int(input('Digite o elemento mat2[%d][%d] ' %(i,j))))
  mat2.append(linha)
print("A segunda matriz é: ", mat2)

if c_mat1 == l_mat2:
  mat_res = []
  for i in range(l_mat1):
    l_res = []
    for j in range(c_mat2):   
      mult = 0
      for k in range(l_mat2):
        mult = mult + (mat1[i][k] * mat2[k][j])
      l_res.append(mult)
    mat_res.append(l_res)
  print(mat_res)
else:
  print('O número de colunas da matriz 1 é diferente do número de linhas da matriz 2, logo não é possível multiplicá-las! ')
  