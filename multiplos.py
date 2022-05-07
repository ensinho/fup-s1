a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
while a == 0 or b == 0:
    print("Entrada inválida! Tente novamente. ")
    a = int(input("Digite um número: "))
    b = int(input("Digite outro número: "))
    while a % b == 0 or b % a == 0:
        print("%d e %d são múltiplos! :)" % (a, b))
        break
    else:
        print("%d e %d não são múltiplos! :( " % (a, b))
