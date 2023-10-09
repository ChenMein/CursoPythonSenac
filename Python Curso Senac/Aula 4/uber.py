proibidas = ['assediada','assédio', 'abusada', 'abuso']
texto = input('Por favor, nos dê seu feedback: ')

resultado = 'assediada' in proibidas

if resultado:
    print('Reclamação atendida. Dentro de alguns dias entraremos em contato.')
    autorizacaoMotorista = False