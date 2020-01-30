def obterContaCurta(conta):
    """
Pega a conta e mostra a forma contrata dela retirando os 0 no final e em seguida,
identa conforme o nível dela.


obs:parametro (conta) deve vir sempre com 11 digitos

Retorna uma string contendo a quantidade de espaços + conta + "."

Parâmetros:
    conta(str)
    
    """
    espaco = ['  ','   ','    ','     ','      ','       ','        ','         ','          ']
    for i in range(len(conta)-1,-1,-1):
        if(conta[i] != '0'):
            break

    contaCurta = conta[:i+1]

    size = len(contaCurta)
    numZeros = 0

    if (size == 3 or size == 5 or size == 8 or size == 10):
        numZeros = 1
    elif (size == 7):
        numZeros = 2
    contaCurta += ('0'* numZeros)

    for i in range(0,9):
        x = espaco[i]
        if size == len(x):
            return x + contaCurta + '.'
            break
        if size == 1:
            return '' + contaCurta +'.'
            break
           

def ordenaConta(Contas):
    """
Ordena as chaves para demonstrar o balancete na ordem correta

Retorna um dicionário onde:
    chave - são as contas
    valores - desc e o saldo

Parâmetros:
    Contas (dic)
    """
    ordem = []
    dic = {}
    for key in sorted (Contas.keys()):
        elemento = key
        ordem.append(elemento)
        
        
    for j in range(len(Contas)):
        chave = ordem[j]
        for l in range(len(Contas)):
            desc = Contas[chave][1]
            saldo = Contas[chave][5]
            dic[chave]=[desc,saldo]
    return dic

