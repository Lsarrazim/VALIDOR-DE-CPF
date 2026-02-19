
cpf = input('Digite um cpf: ')

#verifica se o cpf tem 11 numeros
if len(cpf) != 11:
    print('CPF INVALIDO')
elif not cpf.isdigit():
    print('apenas numeros')
else:

    #vetor com 9 numeros para validação
    conteinerCpf = cpf[:9]
    contagemRegressiva = 10

    #criando os calculos para validação do cpf
    somaMultResultado = 0 

    for digito in conteinerCpf:
        multResultado = (int(digito) * contagemRegressiva)
        somaMultResultado += multResultado
        contagemRegressiva -= 1

    #criando validação do primeiro digito
    primeiroDigito = (somaMultResultado * 10) % 11
    if primeiroDigito > 9:
        primeiroDigito = 0

    #criando a validação do segundo digito
    conteinercpf2 = list(conteinerCpf) + [str(primeiroDigito)]

    somaMultResultado2 = 0
    contagemRegressiva2 = 11

    for digito2 in conteinercpf2:
        MultResultado2 = (int(digito2) * contagemRegressiva2)
        somaMultResultado2 += MultResultado2
        contagemRegressiva2 -= 1

    segundoDigito = (somaMultResultado2 * 10) % 11
    if segundoDigito > 9:
        segundoDigito = 0

    #validor de cpf
    if int(cpf[9]) == primeiroDigito and int(cpf[10]) == segundoDigito:
        print('CPF É VALIDO!')
    else:
        print('CPF É INVALIDO!')









