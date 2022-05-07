import random
print(" JOGO DOS NÚMEROS! - ADVINHE QUAL NÚMERO ESTOU PENSANDO! ")
nv = int(input(
    "--- 1 PARA FACIL ; 2 PARA DIFÍCIL ; 3 PARA INSANO --- Qual nível deseja jogar?  "))
if nv == 1:
    acerto = int(random.randint(1, 10))
    resp = int(input("Em qual número estou pensando?!? "))
    while resp <= 0 or resp > 10:
        print("Entrada inválida! Tente novamente.")
        resp = int(input("Em qual número estou pensando?!? "))
    while resp < acerto:
        print("Resposta incorreta! Tente um numero maior! ")
        resp = int(input("Em qual número estou pensando?!? "))
    while resp > acerto:
        print("Resposta incorreta! Tente um numero menor! ")
        resp = int(input("Em qual número estou pensando?!? "))
    if resp == acerto:
        print("Parabéns você acertou!")
elif nv == 2:
    acerto = int(random.randint(1, 10))
    resp = int(input("Em qual número estou pensando?!? "))
    while resp <= 0 or resp > 10:
        print("Entrada inválida! Tente novamente.")
        resp = int(input("Em qual número estou pensando?!? "))
    for resp in range(2):
        if resp < acerto:
            print("Resposta incorreta! Tente um numero maior! ")
            resp = int(input("Em qual número estou pensando?!? "))
        if resp > acerto:
            print("Resposta incorreta! Tente um numero menor! ")
            resp = int(input("Em qual número estou pensando?!? "))
        if resp == acerto:
            print("Parabéns você acertou!")
    print("Número de tentativas esgotadas...")
elif nv == 3:
    acerto = int(random.randint(1, 10))
    print("--- NÚMERO DE TENTATIVAS: 3 ---")
    resp = int(input("Em qual número estou pensando?!? "))
    while resp <= 0 or resp > 10:
        print("Entrada inválida! Tente novamente.")
        resp = int(input("Em qual número estou pensando?!? "))
    for resp in range(2):
        if resp != acerto:
            print("Resposta incorreta! ")
            resp = int(input("Em qual número estou pensando?!? "))
        if resp == acerto:
            print("Parabéns você acertou!")
    print("Número de tentativas esgotadas...")
else:
    print("Nível não existente!")
