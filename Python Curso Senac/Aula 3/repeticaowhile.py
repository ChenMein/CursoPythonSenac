i = 1
# m = int(input('Digite um número para gerar sua tabuada: '))
resp = 's'

"""
while i < 10:   # enquanto i menor 10
    print(i)
    i = i + 1
    
while i <= 10:  # enquanto i menor ou igual 10
    print(i)
    i = i + 1
"""

while resp == 's':
    m = int(input('Digite o valor da tabuada: '))
    while i <= 10:
        print(i, 'x', m, '=', i * m)
        i = i + 1

    resp = input('Quer continuar? s ou n: ')
