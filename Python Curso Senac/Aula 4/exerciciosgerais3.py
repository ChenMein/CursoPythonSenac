import random

numerosorteado = random.randint(1, 10) # randint limita para que sejam sorteados apenas números inteiros
chute = int(input('Qual seu chute de 1 a 10? '))
resp = 's'

print('-' * 40)

print('Número sorteado pelo sistema: ', numerosorteado)

print('-' * 40)

while resp == 's':
    if chute == numerosorteado:
        print(f'Aposta do usuário: {chute}')
        print('Parabéns, você acertou! :D')
    else:
        print(f'Aposta do usuário: {chute}')
        print('Poxa, você não acertou... :(')
        print('-' * 40)
    resp = input('Deseja continuar? s ou n: ')

"""
    EXTRA PARA CASA:
    - CONTAR QUANTAS TENTATIVAS ATÉ ACERTAR
    - LIMITAR TENTATIVAS
"""