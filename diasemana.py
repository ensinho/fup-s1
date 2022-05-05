nc = int(input('qual o numero correspondente? '))
if nc > 0 and nc < 8:
    if nc==1:
        print('domingo')
    elif nc==2 :
        print('segunda')
    elif nc==3:
        print('terça')
    elif nc==4:
        print('quarta')
    elif nc==5:
        print('quinta')
    elif nc==6:
        print('sexta')
    elif nc==7:
        print('sabado')

    else:
        print('numero invalido')    