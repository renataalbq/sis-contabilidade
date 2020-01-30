from fmsg import *

def export_contas(Contas,nome_arq):
    """
Exporta os dados contidos no dicionário de Contas em arquivo CSV, com carácter de separação '\t'

Parâmetros:
    Contas(dic)

    """
    arq = open(f'{nome_arq}.csv', 'w')

    for conta in Contas:
        cont = 0
        for i in conta:
            cont += 1
            arq.write(str(i))
            if cont < len(conta):
                arq.write('\t')

        arq.write('\n')

    print(f'\nDados se encontram em: "{nome_arq}.csv" ')
    mensagem('EXPORTACAÇÃO FEITA COM SUCESSO !')
    arq.close()


def export_mov(Mov,nome_arq):
    """
Exporta os dados contidos no dicionário de Movimentação em arquivo CSV, com carácter de separação '\t'

Parâmetros:
    Mov(dic)

    """
    arq = open(f'{nome_arq}.csv', 'w')
    for mov in Mov:
        cont = 0
        for i in mov:
            cont += 1
            arq.write(str(i))
            if cont < len(mov):
                arq.write('\t')
        arq.write('\n')

    print(f'\nDados se encontram em: "{nome_arq}.csv" ')
    mensagem('EXPORTACAÇÃO FEITA COM SUCESSO !')
    arq.close()




def import_contas(nome_arq):
    """
Importa os dados contidos no arquivo csv, com carácter de separação '\t, inserindo
os dados para dentro do dicionário Contas.

A seguinte função retorna duas tuplas distintas dependendo do seguinte caso:

    1 - caso o usuário forneça um nome de arquivo que não consta no arquivo local a
      função retornará a tupla : ('Nome do arquivo não existe',flag)

    2 - caso contrário a função retornará: (Contas,flag)

    A flag aparece nos dois casos e ela sai com valores Booleanos( True ou False) dependendo
    dos casos citados acima.


nome_arq é parâmetro dado pelo usuário informando o nome do arquivo


Parâmetros:
    nome_arq(str)

    """
    
    Contas = []
    dic_Contas = {}
    flag = True
    try:
        arq = open(f'{nome_arq}.csv','r')
    except FileNotFoundError:
        flag = False
        return ('Nome do arquivo não existe',flag)
    if flag:   
        for linha in arq.readlines():
            tokens = linha.split('\t')
            Contas.append(tokens)

        for i in range (len(Contas)):
            chave = Contas[i][0]
            dig = Contas[i][1] 
            desc = Contas[i][2].lower()
            tipo = Contas[i][3].lower()
            total_deb = float(Contas[i][4])
            total_cred = float(Contas[i][5])
            saldo = Contas[i][6]
            saldo = saldo[:-1].replace('\n','')
            
            dic_Contas[chave] =[dig,desc,tipo,total_deb,total_cred,float(saldo)]

        Contas = dic_Contas
        mensagem('IMPORTAÇÃO FEITA COM SUCESSO !')
        arq.close()

        return (Contas,flag)

    if flag == False:
        print('Arquivo inexistente')


def import_mov(nome_arq):
    """
Importa os dados contidos no arquivo csv, com carácter de separação '\t, inserindo
os dados para dentro do dicionário Contas.

A seguinte função retorna duas tuplas distintas dependendo do seguinte caso:

    1 - caso o usuário forneça um nome de arquivo que não consta no arquivo local a
      função retornará a tupla : ('Nome do arquivo não existe',flag)

    2 - caso contrário a função retornará: (Mov,flag)

    A flag aparece nos dois casos e ela sai com valores Booleanos( True ou False) dependendo
    dos casos citados acima.


nome_arq é parâmetro dado pelo usuário informando o nome do arquivo


Parâmetros:
    nome_arq(str)

    """
    Mov = []
    dic_Mov = {}
    flag = True
    try:
        arq =open(f'{nome_arq}.csv','r')
    except FileNotFoundError:
        flag = False
        return ('Nome do arquivo não existe',flag)
        
    if flag:
        for linha in arq.readlines():
            tokens = linha.split('\t')
            Mov.append(tokens)       

        for i in range (len(Mov)):
            chave = int(Mov[i][0])
            data = Mov[i][1]
            conta_cred = Mov[i][2]
            dig_cred = Mov[i][3]
            conta_deb = Mov[i][4]
            dig_deb = Mov[i][5]
            desc = Mov[i][6].lower()
            saldo = Mov[i][7]
            saldo = saldo[:-1].replace('\n','') 
            dic_Mov[chave] =[data,conta_cred,dig_cred,conta_deb,dig_deb,desc,float(saldo)]
    
        Mov = dic_Mov
        mensagem('IMPORTAÇÃO FEITA COM SUCESSO !')
        arq.close()
        return (Mov,flag)




def checagem_arquivo_mov(tupla,Mov):
    """
Checa a saida da função import_mov e decide se:
    1 - dará uma mensagem de que o arquivo é inexistente;
    2 - Fará a importação a partir do nome do arquivo fornecido;

Parâmetros:
    tupla(tuple)
    Mov(dic)
    """
    if False in tupla:
        print(tupla[0])
    if True in tupla:
        Mov.update(tupla[0])


def checagem_arquivo_Contas(tupla,Contas):
    """
Checa a saida da função import_contas e decide se:
    1 - dará uma mensagem de que o arquivo é inexistente;
    2 - Fará a importação a partir do nome do arquivo fornecido;

Parâmetros:
    tupla(tuple)
    Contas(dic)
    """
    if False in tupla:
        print(tupla[0])
    if True in tupla:
        Contas.update(tupla[0])
        
