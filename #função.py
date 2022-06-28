from unittest import result
# função paridade


def calculo(par):
    if numero % 2 == 0:
        return True
    else:
        return False

# função positivo


def positivo(num):
    if numero > 0:
        return True
    else:
        return False

# função cont_regressiva


def regress(int):
    for i in range(i, -1, -1):
        print(i)

# função frase


def subst(fra):
    a = fra.replace(' ', '#')
    return a

# função entrada frase


def entrada(f):
    frase = input("Digite sua frase aqui: ")
    return frase

# função contagem palavras


def contagem(palavras):
    b = frasal.count(' ')
    c = b + 1
    return c


# programa principal numeros
'''numero = int(input("Digite um numero para conferir sua paridade "))
result = calculo(numero)
print("Seu número é par! ", result)'''

# programa principal frase

'''frase1 = entrada(result)
print(frase1)

troca = subst(frase1)
print(troca)'''

# programa principal frase-palavras
'''frasal = input("Digite sua frase aqui chefia: ")
frasel = contagem(frasal)
print("A quantidade de palavras é de : ", frasel)'''
