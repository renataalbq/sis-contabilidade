def processamento(Contas,saldo_mov, conta_mov, operacao):
    """
Atualização financeira. Analisa as contas onde foram feita as movimentações e transfere elas para
o saldo total de débito, total de crédito e saldo total, realizando as modificações para as respectivas
contas superiores.

A operação poderá ser de débito ou de crédito ( 'C' ou 'D') definida no parâmetro operacao

Parâmetros:
Contas(dic)
saldo_mov(float)
conta_mov(float)
operacao(str)
    """
    

    if(operacao == 'D'):
        Contas[conta_mov][4] += saldo_mov
        Contas[conta_mov][5] -= saldo_mov

    else:
        Contas[conta_mov][3] += saldo_mov
        Contas[conta_mov][5] += saldo_mov

    for k, v in Contas.items():
    
        conta_formatamov = '{}.{}.{}{}.{}{}.{}{}{}.{}{}'.format(*conta_mov)
        conta_formataconta = '{}.{}.{}{}.{}{}.{}{}{}.{}{}'.format(*k)
        splitedconta_Mov = conta_formatamov.split('.')
        splitedconta = conta_formataconta.split('.')

    #Inicio das comparações com a conta do indice
        for i in range(len(splitedconta)):
      #Condição para não dar com a condição dentro do if menor (i+1), caso não fizesse essa
            #checagem daria que o array não tem essa posição
          if(i < 5):
        #Comparando posição a posição se é igual da conta movimentada e a conta que está
              #sendo percorrida por nivel, cada posição que "i" assume é um nivel de conta. 
        #(começando por 0), checando se o proximo nivel da conta é diferente e tambem se o
              #proximo nivel da conta candidata a ser "pai" é 0.
            if ((splitedconta[i] == splitedconta_Mov[i])
              and (splitedconta[i+1] != splitedconta_Mov[i+1])
              and (splitedconta[i+1] == '0'*len(splitedconta[i+1]))):
                conta_superior = ''.join(splitedconta)
                if(operacao == 'D'):
                    #Contas[conta_superior][4] += saldo_mov
                    Contas[conta_superior][5] -= saldo_mov
                else:
                    #Contas[conta_superior][3] += saldo_mov
                    Contas[conta_superior][5] += saldo_mov
          
            else:
              continue


def total(Contas):
    """
Varre o dicionário Contas e soma todos os saldo-débito e os saldo-crédito, e em seguida subtrai esses valores para gerar
a Receita. No final guarda essas informações em uma lista

A função retorna um lista contendo: O total de despesas e o Total de Receitas e o saldo final.

Parâmetros:
Contas(dic)
    """

    saldodeb = 0
    saldocred = 0
    saldo_final = 0

    for i in Contas:

        saldodeb += Contas[i][4]
        saldocred += Contas[i][3]
    saldo_final = saldocred - saldodeb

    lista = [saldodeb, saldocred, saldo_final]

    return lista

def zera_contas(Contas):
    """
Zera o saldo débito, saldo crédito e o saldo total de todas as contas do dicionário.

Parâmetros:
Contas(dic)
    """

    for i in Contas:
        Contas[i][3] = 0.00
        Contas[i][4] = 0.00
        Contas[i][5] = 0.00
        
    
