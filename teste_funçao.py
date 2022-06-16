# função do programa
def calculo(sal):
    perc = float(input('Digite o aumento do salario: '))
    valor = sal * perc / 100
    return valor


# programa principal
sal = float(input("Qual o valor do salario? "))
aum = calculo(sal)
novsal = sal + aum
print('O novo salario é: ', novsal)
