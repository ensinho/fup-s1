peso = float(input('Quantos quilos foram pescados hoje? '))
if (0 < peso <= 50):
    print('Você pescou dentro do limite de pesca de SP!')
elif peso > 50:
    multa = (peso-50)*4
    print('Você pescou indevidamente. Multa atual = ', multa)
else:
    print('Você não pescou nada!')
