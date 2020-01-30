# Função da crítica do movimento

def critica_movimento(registro,Contas,saldo_mov,conta_deb,conta_cred,digito_mov_deb,digito_mov_cred):
    """
Realiza a crítica do movimento a partir das movimentações que foram armazenadas
no dicionário de movimentacao e checa se existem erros.

A funcao retorna uma tupla nesse formato : (constatacao,errosDetectados)
constatacao(str) - concatenação das diversas mensagens de erro
errosDetectados(bool) - flag que pode sair com True ou False dependendo
da seguinte situação:
    - Caso a flag saia como False, significa que não houve erros na movimentacao;
    - Caso a flag saia com True, significa que existem erros na movimentacao;

    Portanto as possibilidades que podemos ter dentro da tupla são duas -
    1- string vazia na primeira posição e False na segunda
    2- string na primeira posição e True na segunda

Parâmetros:
registro(int)
Contas(dic)
saldo_mov(float)
conta_deb(str)
conta_cred(str)
digito_mov_deb(str)
digito_mov_cred(str)
    """
    errosDetectados = False
    constatacao = ''

    if saldo_mov == 0: 
        constatacao += f'\nRegistro: {registro}    Valor Nulo'
        errosDetectados = True

    if conta_deb == '' and conta_cred == '': 
        constatacao += f'\nRegistro: {registro}    Sem Conta para Movimentação'
        errosDetectados = True

    if conta_deb in Contas:
        tipo_conta = Contas[conta_deb][2]
        digito_conta = Contas[conta_deb][0]

        if tipo_conta == 's':
            constatacao += f'\nRegistro: {registro}    Conta Débito Sintética'
            errosDetectados = True

        if digito_mov_deb != digito_conta:
            constatacao += f'\nRegistro: {registro}    Dígito da Conta Débito Inválida'
            errosDetectados = True
                
    if conta_cred in Contas:
        tipo_conta = Contas[conta_cred][2]
        digito_conta = Contas[conta_cred][0]

        if tipo_conta == 's':
            constatacao += f'\nRegistro: {registro}    Conta Crédito Sintética'
            errosDetectados = True

        if digito_mov_cred != digito_conta:
            constatacao += f'\nRegistro: {registro}    Dígito da Conta Crédito Inválida'
            errosDetectados = True

    if conta_deb not in Contas and conta_deb != '':
        constatacao += f'\nRegistro: {registro}    Conta Débito inexistente'
        errosDetectados = True                

    if conta_cred not in Contas and conta_cred != '':
        constatacao += f'\nRegistro: {registro}    Conta Crédito inexistente'
        errosDetectados = True

    situacao =(constatacao,errosDetectados) 

    return situacao
    

    

        
