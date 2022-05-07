ano = int(input("Digite um ano para conferir se é bissexto: "))
if ano % 400 == 0:
    print("É bissexto! ")
elif ano % 100 == 0:
    print("Não é bissexto! ")
elif ano % 4 == 0:
    print("É bissexto! ")
else:
    print("Não é bissexto! ")
