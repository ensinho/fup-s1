q1 = int(input('Digite 1 para SIM e 2 para NÃO - telefonou para a vitima? '))
q2 = int(input('esteve no local do crime? '))
q3 = int(input('mora perto da vitima? '))
q4 = int(input('devia para a vitima? '))
q5 = int(input('ja trabalhou com a vitima? '))
r = (q1 + q2 + q3 + q4 + q5)
if r == 2:
    print('Pessoa classificada como suspeita! ')
elif r >=3 and r <=4:
    print('Pessoa classificada como cumplice! ')
elif r == 5:
    print('pessoa classificada como assassina!')
else:
    print("pessoa inocente")