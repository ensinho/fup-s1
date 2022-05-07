preço = int(input("Qual o preço do produto? "))

if preço > 0:
    npc = int(input("Qual o número de parcelas? "))
    if npc == 1:
        print("Então o valor do produto permanecerá em %d sem acréscimos. " % preço)
    elif npc == 2:
        preço = preço*1.07
        pc = preço/2
        print("O valor do produto com o acréscimo é de %.2f e cada parcela será R$ %.2f  " % (
            preço, pc))
    elif npc == 3:
        preço = preço*1.1
        pc = preço/3
        print("O valor do produto com o acréscimo é de %.2f e cada parcela será R$ %.2f " % (
            preço, pc))
    else:
        print("Número de parcelas não aceito.")
else:
    print("Preço inválido.")
