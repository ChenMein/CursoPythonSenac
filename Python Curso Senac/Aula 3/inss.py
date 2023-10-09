salario = float(input('Informe seu salário: '))
op = input('Recebe VT s ou n? ')

if salario <= 1320:                                 # sempre abre
    if op == "s":
        vt = salario * 0.06
        inss = salario * 0.075
        print('Desconto do INSS: ', inss)
        print('Desconto VT: ', vt)
        print('Salário líquido: ', salario - inss - vt)
    else:
        vt = 0
        inss = salario * 0.075
        print('Desconto do INSS: ', inss)
        print('Salário líquido: ', salario - inss)

elif salario >= 1320.01 and salario <= 2571.29:     # sempre no meio
    if op == "s":
        vt = salario * 0.06
        inss = salario * 0.09
        print('Desconto do INSS: ', inss)
        print('Desconto VT: ', vt)
        print('Salário líquido: ', salario - inss - vt)
    else:
        vt = 0
        inss = salario * 0.09
        print('Desconto do INSS: ', inss)
        print('Salário líquido: ', salario - inss)

elif salario >= 2571.30 and salario <= 3856.94:
    if op == "s":
        vt = salario * 0.06
        inss = salario * 0.12
        print('Desconto do INSS: ', inss)
        print('Desconto VT: ', vt)
        print('Salário líquido: ', salario - inss - vt)
    else:
        vt = 0
        inss = salario * 0.12
        print('Desconto do INSS: ', inss)
        print('Salário líquido: ', salario - inss)

elif salario >= 3856.95 and salario <= 7507.49:
    if op == "s":
        vt = salario * 0.06
        inss = salario * 0.14
        print('Desconto do INSS: ', inss)
        print('Desconto VT: ', vt)
        print('Salário líquido: ', salario - inss - vt)
    else:
        vt = 0
        inss = salario * 0.14
        print('Desconto do INSS: ', inss)
        print('Salário líquido: ', salario - inss)
else:                                               # sempre fecha
    if op == "s":
        vt = salario * 0.06
        inss = 7507.49 * 0.14
        print('Desconto do INSS: ', inss)
        print('Desconto VT: ', vt)
        print('Salário líquido: ', salario - inss)
    else:
        vt = 0
        inss = 7507.49 * 0.14
        print('Desconto do INSS: ', inss)
        print('Salário líquido: ', salario - inss)