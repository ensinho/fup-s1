from ast import NotIn
import string
# alfabeto em modo de lista
alfabeto = list(string.ascii_uppercase)

# entrada de dados da quantidade, com tratamento
while True:
    num = int(input("Quantos peixes existem no aquario? "))
    if num > 0:
        break
    else:
        print("Entrada inválida! Tente Novamente!")

peixes = []
i = 0

# entrada de dados das especies, com tratamento
while i < num:
    peixe = input("Digite a espécie do Peixe: ")
    if peixe.upper() in alfabeto:
        peixes.append(peixe.upper())
        i += 1
    else:
        print("Espécie inválida! ")

especies = []


# testando para nao repetir elementos!
for peixe in peixes:
    if peixe not in especies:
        especies.append(peixe)
print(especies)
