"""
a1 = input('Digite o nome: ')
a2 = input('Digite o nome: ')
a3 = input('Digite o nome: ')
a4 = input('Digite o nome: ')
a5 = input('Digite o nome: ')
"""

"""
Método sem listas; substitui uma entrada por outra, não armazena o que foi listado
i = 1
while i <= 3:
    titular = input('Digite o nome do titular: ')
    i = i + 1
    print(titular)
"""
lista = ['Ana', 'Joao', 'Maria']
existe = 'Ana' in lista
print(existe)

print('-' * 20)

bairro = ['Copacabana', 'Botafogo', 'Glória', 'Flamengo']
existe = input('Seu bairro está cadastrado? ').title()
resultado = existe in bairro
if resultado:
    print('Sim, bairro cadastrado!')
else:
    print('Não, bairro não cadastrado...')