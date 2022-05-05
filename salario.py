salario =  float(input('qual o seu salario? '))
aumento = int(input('qual o aumento em porcentagem? '))
an = salario*aumento/100 
sff = an + salario 
if salario > 0 or aumento > 0: 
    if sff>3000:
        print('salario inacessivel')
    elif sff=<3000:
        ('o aumento sera de ',an)
        ('o salario com aumento sera de ', round(sff,2))
else:
    print('entradas invalidas')