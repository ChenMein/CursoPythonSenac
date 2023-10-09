"""
Crie um programa que calcule o valor de um carro
somando a ele o IPI de 3.5%, se o valor for maior que 40000
Senão o valor do IPI será de 7.5%
"""

carro = float(input('Informe o valor do carro: R$'))

if carro >= 40000:
    ipi = carro * 0.035
    print(f'Valor ICMS: R${ipi}')
    print('Valor do carro com ICMS incluso: R$', ipi + carro)

else:
    ipi = carro * 0.075
    print(f'Valor ICMS: R${ipi}')
    print(f'Valor do carro com ICMS incluso: R${ipi + carro}')