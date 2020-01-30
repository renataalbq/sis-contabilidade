# Formatação da conta/ Cálculo do dígito...

def completazero(conta):
    """
Pega a conta fornecida pelo usuário e completa com zeros sem ulrapassar o tamanho
máximo da conta (11 carácteres).

Parâmetros:
    conta(str)
    """
    conta_final = conta + ('0' * (11-len(conta)))
    return conta_final

def calculadigito (conta):
    """
Pega a conta fornecida pelo usuário e faz o cálculo do dígito.

obs: Parâmetro conta deve vir sempre com 11 dígitos

Parâmetros:
    conta(str)
    """

    pesos = '27654327654'
    soma = 0
    n = conta

    for i in range(0,11):
        soma += int(n[i]) * int(pesos[i])

    resto = soma % 11

    dv = 11 - resto
    if dv == 10:
        dv = 0

    elif dv == 11:
        dv = '&'

    return dv


def separaconta(conta):
    """
Pega a conta fornecida pelo usuário e formata ela no padrão correto separados por ponto.
exemplo:
    1.0.00.00.000.00

obs: Parâmetro conta deve vir sempre com 11 dígitos

Parâmetros:
    conta(str)

    """
    n = conta
    conta_formatada = f'{n[0]}.{n[1]}.{n[2]}{n[3]}.{n[4]}{n[5]}.{n[6]}{n[7]}{n[8]}.{n[9]}{n[10]}'
    


