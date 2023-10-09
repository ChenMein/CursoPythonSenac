"""
Comandos condicionais
-> If(se) - verifica uma confição e faz desvio da execução do programa

php
if (idade>18){
    echo "maior de 18";
}

java
if (idade>18){
    System.out.printin("maior de 18");
}
"""

idade = int(input('Digite a sua idade: '))
if idade > 18:                              # se idade for maior que 18, então
    print('Ah, és maior de idade ₍ᐢ•⩊•ᐢ₎')   # resposta verdadeira
elif idade == 18:
    print('Tens 18 anos ε(´｡•᎑•`)っ 💕')
else:                                       # senão
    print('Hm, és menor de idade ₍ᐢ._.ᐢ₎')    # resposta falsa; negação das duas anteriores