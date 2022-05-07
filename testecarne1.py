print('DIGITE 1 PARA SIM E 0 PARA NÃO NAS REPSPOSTAS ')
p1 = int(input('A carne esta com gordura branca e firme? '))
p2 = int(input('A carne possui cor vermelho-brilhante? '))
p3 = int(input('A carne está em temperatura inferior a 7 graus? '))
p4 = int(input('A carne possui cheiro agradável? '))
p5 = int(input('A carne ainda está dentro do prazo de validade? '))
sp = (p1+p2+p3+p4+p5)
if p5 == 0:
    print('A carne reprovou no teste! ')
else:
    if sp > 3:
        print('A carne passou no teste! ')
    else:
        print('A carne reprovou no teste! ')
