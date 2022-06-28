lin_mat1 = int(input("Digite as linhas da matriz 1: "))
col_mat1 = int(input("Digite as colunas da matriz 1: "))

#lin_mat2 = int(input("Digite as linhas da matriz 2: "))
#col_mat2 = int(input("Digite as colunas da matriz 2: "))


# <-- preench mat1 -->
mat1 = []
for i in range(lin_mat1):
    linha = []
    for j in range(col_mat1):
        linha.append(int(input(f"Digite o elemento mat1[{i}][{j}]")))
    mat1.append(linha)
print("A primeira matriz é: ", mat1)


# <-- preench mat2 --> 
#mat2 = []
#for i in range(lin_mat2):
#    linha = []
#    for j in range(col_mat2):
#        linha.append(int(input(f"Digite o elemento mat1[{i}][{j}]")))
#    mat2.append(linha)
#print("A segunda matriz é: ", mat2)


# <-- calculo determinante matriz 2x2 -->
#for i in range(2):
#    for j in range(2):
#        if i == j:
#            det = ((mat1[0][0] * mat1[1][1])-(mat1[0][1] * mat1[1][0]))
#        else: continue
#print("A determinante é: ",det)


# <-- calculo determinante matriz 3x3 --> 

colunas = mat1.copy()
print(colunas) 
colunas.remove(colunas[0][2])
#colunas.remove(mat1[1][2])
#colunas.remove(mat1[2][2])


