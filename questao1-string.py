curso = 'Programação em Python'

#a)
a = curso.count(' ')
b = len(curso)-a
print(b)

#b) 
print('prog' in curso)

#c)
print('i' in curso)
print('I' in curso)

#d)
print(curso.count('o'))
print(curso.count('O'))

#e) f)
print(curso.rfind('o'))
print(curso.find('o'))

#g)
c = curso.split()
py = c[-1]
py2 = py.lower()
py3 = sorted(py2)
#usar * para só imprimir os elementos
print(*py3)

#h)
print(curso.replace('Python', 'Java'))
