def transformatriz_contas(Contas):
    """
Transforma o dicionário Contas em um list para que possa ser exportado em formato CSV.

A função retorna um list.

Parâmetros:
Contas(dic)

    """
    chaves = []
    valores = []
    matriz = []
    for i in Contas:
        chaves.append(i)
        valores.append(Contas[i])

    for j in range (len(valores)):
        dig = valores[j][0]
        desc = valores[j][1]
        tipo = valores[j][2]
        total_deb = valores[j][3]
        total_cred = valores[j][4]
        saldo = valores[j][5]
        matriz.append([dig,desc,tipo,total_deb,total_cred,saldo])

    for k in range(len(matriz)):
        matriz[k].insert(0,chaves[k])

    return matriz


def transformatriz_mov(Mov):
    """
Transforma o dicionário Mov em um list para que possa ser exportado em formato CSV.

A função retorna um list.

Parâmetros:
Mov(dic)

    """
    chaves = []
    valores = []
    matriz = []

    for i in Mov:
        chaves.append(i)
        valores.append(Mov[i])


    for j in range (len(valores)):
        data = valores[j][0]
        conta_deb = valores[j][1]
        dig_deb = valores[j][2]
        conta_cred = valores[j][3]
        digito_cred = valores[j][4]
        desc = valores[j][5]
        valor = valores[j][6]
        matriz.append([data,conta_deb,dig_deb,conta_cred,digito_cred,desc,valor])

    for k in range(len(matriz)):
        matriz[k].insert(0,chaves[k])

    return matriz
    
    
