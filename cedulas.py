import math
valor = int(input('Qual o valor a ser retirado? '))
if valor > 0 and valor < 1000000:
    nota100 = valor//100
    resto100 = valor % 100
    nota50 = resto100//50
    resto50 = resto100 % 50
    nota20 = resto50//20
    resto20 = resto50 % 20
    nota10 = resto20//10
    resto10 = resto20 % 10
    nota5 = resto10//5
    resto5 = resto10 % 5
    nota2 = resto5//2
    resto2 = resto5 % 2
    nota1 = resto2//1
    print('Valor a ser retirado em notas de RS100: ', nota100, ' Em notas de R$50: ', nota50, 'Em notas de R$20: ',
          nota20, 'Em notas de R$10: ', nota10, 'Em notas de R$5: ', nota5, 'Em notas de R$2: ', nota2, 'Em notas de R$1: ', nota1)
else:
    print('Variáveis inválidas!')
