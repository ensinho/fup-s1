num = input("digite seu número: ")
n = num.split()
if len(n) < 9:
    n.insert(0,9)
    print("Numero corrigido com o 9: - ", n)
