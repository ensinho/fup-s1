#tamanho do nome digitado:
'''nome = input('Qual seu nome completo? ')
print(len(nome))'''

#conferir se começa com o elemento digitado:
'''curso = 'Ciência da CompUtação'
print(curso.startswith('Ci'))
print(curso.upper())
print(curso.startswith('Cie'))'''

#o In e o not in conferem se esta dentro lower para por tudo em capslock:
'''turma = 'Turma 2A de Fundamentos de Programação '
print('Fup' in turma )
print('Prog' in turma )
print('2a' in turma.lower())'''

#count para contar quantos elementos têm: 
'''frase = 'O sabiá não sabia o que o sábio sabia que o sabiá não sabia assobiar'
print(frase.count('sabiá'))
print(frase.count('sabia'))
print(frase.count('sábio'))
print(frase.count('s'))'''

#o find busca da esquerda pra direita:
'''frase = 'O sabiá não sabia que o sábio sabia que o sabiá não sabia assobiar'
print(frase.find('sabia'))
print(frase.find('sabia',13))
print(frase.find('sabia',13,30))
print(frase.find('sabia',13,35))'''

#O rfind busca da direita pra esquerda: 
'''frase = 'O sabiá não sabia que o sábio sabia que o sabiá não sabia assobiar'
print(frase.rfind('sabia'))
print(frase.rfind('sabia',13))
print(frase.rfind('sabia',13,30))
print(frase.rfind('sabia',13,35))'''

#O split transforma a string em uma lista
'''a = 'ciencia da computação'
print(a.split())'''

#separando split com separador
'''frase = 'segunda,terça,quarta'
print(frase.split(','))'''

#utilizando replace 
'''print(frase.replace('quarta', 'quinta '))'''
