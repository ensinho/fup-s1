import math
pesoa = int(input('Qual foi a gramagem de ração vendida no tipo A? '))
pesob = int(input('Qual foi a gramagem de ração vendida no tipo B? '))
pesoc = int(input('Qual foi a gramagem de ração vendida no tipo C? '))
if pesoa > 0:
    kga = math.floor(pesoa/1000)*5
    ga = (pesoa % 1000)
    if ga > 500:
        ga = 2.5
    elif ga < 500:
        ga = 0
    lucroa = kga + ga
    print("O lucro do tipo A foi de %.2f " % lucroa)
else:
    print("Não houve lucros do tipo A!")
if pesob > 0:
    lucrob = math.floor(pesob/1000)*2.5
    print("O lucro do tipo B foi de %.2f " % lucrob)
else:
    print("Não houve lucros do tipo B!")
if pesoc > 0:
    lucroc = math.floor(pesoc/1000)*0.5
    print("O lucro do tipo C foi de %.2f " % lucroc)
else:
    print("Não houve lucros do tipo C!")
