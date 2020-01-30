from time import sleep
from datetime import date
from fmsg import *
from fcritica import *
from fformataconta import *
from fprocessa import *
from farquivo import *
from fbalancete import *
from ftransformadic import *


Contas = {}
Mov = {}
opcao = ''
contador_registro = 0
contaCadastrada = False
movimentacaoCadastrada = False
errosDetectados = False
constatacao = ''
controle = 0
ultimoregistro = 0


while opcao != 's':
    menu()
    opcao = input('\nDigite a opção desejada:').lower()

    if opcao == 'c':
        mensagem('CADASTRAR CONTA')
        

        while True:
            conta = str(input('Número da conta (Digite 0 se deseja sair): ')).strip()
            

            if conta == '0':
                retorno()
                
                break
            
            if conta.isnumeric():
                n = completazero(conta)
                digito = str(calculadigito(n))
                conta_formatada = f'{n[0]}.{n[1]}.{n[2]}{n[3]}.{n[4]}{n[5]}.{n[6]}{n[7]}{n[8]}.{n[9]}{n[10]} - {digito}'

                if conta == '00000000000':
                    print('Conta Inválida')
                    break

                if conta in Contas.keys():
                    print(f'Conta {n} já cadastrada ')
                    retorno()
                    break

                print(conta_formatada)

                desc = input('Descrição da conta: ')
                while True:
                    tipo = input('Tipo da conta [A = Analítica / S = Sintética]: ').lower()

                    if tipo == 's' or tipo == 'a':
                        break

                print(f'Total de crédito: {0:6.2f} ')
                print(f'Total de débito: {0:6.2f} ')
                print(f'Saldo: {0:6.2f} ')
                sleep(1)

                while True:
                    resp = input('Deseja cadastrar a conta?\n[S / N]: ').lower()

                    if resp == 'n':
                        break

                    elif resp == 's':
                        sleep(1)
                        mensagem('CONTA CADASTRADA')
                        Contas[n] = [digito, desc, tipo, 0, 0, 0]
                        contaCadastrada = True
                        break
            else:
                print('Número da conta inválida')

    if contaCadastrada==True or opcao=='i':
        if opcao == 'd':
            mensagem('MOVIMENTAÇÃO FINANCEIRA')

            while True:
                resp = input('ENTER para iniciar a movimentação  /  Digite 0 para retornar ao menu ')

                if resp == '0':
                    retorno()
                    break

                elif resp == '':

                    dig_contadeb = ''
                    dig_contacred = ''
                    dt = date.today()
                    data = f'{dt.year}/{dt.month}/{dt.day}'
                    print(f'\nData: {data}\n')

                    contadeb = (input('Conta de Débito:'))
                    if contadeb != '':
                        contadeb = completazero(contadeb)
                        dig_contadeb = input('Dígito: ')

                    contacred = (input('Conta de Crédito: '))
                    if contacred != '':
                        contacred = completazero(contacred)
                        dig_contacred = input('Dígito: ')

                    valor = str(input('Quantia a ser movimentada: '))
                    if valor.isnumeric():
                        valor = float(valor)
                    else:
                        valor = 0

                    descc = input('Descrição complementar: ')
                    print()
                    resp = input('Deseja cadastrar a movimentação?\n[S / N]: ').lower()

                    if resp == 'n':
                        retorno()
                        break

                    elif resp == 's':
                        if len(Mov) != 0:
                            for i in Mov:
                                ultimoregistro = i
                            contador_registro = ultimoregistro + 1
                            Mov[contador_registro] = [data, contadeb, dig_contadeb, contacred, dig_contacred, descc, valor]
                        else:
                            contador_registro += 1
                            Mov[contador_registro] = [data, contadeb, dig_contadeb, contacred, dig_contacred, descc, valor]

                        movimentacaoCadastrada = True

                        print(f'''\n 
    Número do registro: {contador_registro}
    Data: {data}
    Conta débito: {contadeb}-{dig_contadeb}
    Conta crédito: {contacred}-{dig_contacred}
    Valor: R$ {valor:6.2f}
    Descrição: {descc}\n''')
                    sleep(1)
                    mensagem('MOVIMENTAÇÃO CADASTRADA')
                    sleep(1)

        elif opcao == 'a' or opcao == 'p':
            
            while True:
                constatacao = ''

                for i in range(1, len(Mov)+1):
                    registro = i
                    saldo_mov = Mov[i][6]
                    conta_deb = Mov[i][1]
                    conta_cred = Mov[i][3]
                    digito_mov_deb = Mov[i][2]
                    digito_mov_cred = Mov[i][4]
                                
                    situacao = critica_movimento(registro, Contas, saldo_mov, conta_deb, conta_cred, digito_mov_deb, digito_mov_cred)
                    constatacao += situacao[0]
    
                if opcao == 'p':
                    mensagem('PROCESSAR MOVIMENTO')

                    try:

                        if True in situacao:
                            print(f'Não foi possível iniciar o Processamento:\nErro na Movimentação')
                            retorno()
                            break

                        else:
                            print('INICIANDO ATUALIZAÇÃO ...')
                            zera_contas(Contas)
                            for i in range(1, len(Mov)+1):

                                conta_deb = Mov[i][1]
                                conta_cred = Mov[i][3]
                                saldo_mov = Mov[i][6]
                                    
                                    # Débito
                                if conta_deb != '':
                                    processamento(Contas, saldo_mov, conta_deb, 'D')

                                    # Crédito
                                if conta_cred != '':
                                    processamento(Contas, saldo_mov, conta_cred, 'C')


                            mensagem('PROCESSAMENTO FEITO COM SUCESSO !')

                            retorno()
                            break

                    except NameError:

                        print('Não há movimentação em contas para atualizar')
                        retorno()
                        break

                if opcao =='a':
                    mensagem('CRÍTICA DO MOVIMENTO FINANCEIRO')

                    try:
                        if False in situacao:
                            print(f'Crítica do Movimento não contém erros')
                            retorno()
                            break

                        if True in situacao:

                            print(f'\n{"#":<3}{"Data":<11}{"Conta de Débito":<16} {"Conta de Crédito":<16} {"Valor":>10}')
                            print("-" * 58)
                            for i, registro in enumerate(Mov):
                                print(f'{i+1:<2} {Mov[registro][0]:<11} {Mov[registro][1]:<11}-{Mov[registro][2]:<5} {Mov[registro][3]:<11}-{Mov[registro][4]:<5} {Mov[registro][6]: >7.2f}')
                            print(constatacao)
                            print()

                            resp = input('Deseja fazer alteração? [S/N]: ').lower()

                            if resp == 'n':
                                retorno()
                                break

                            elif resp == 's':

                                while True:

                                    registro = int(input('Número do Registro (Digite 0 pra sair):'))

                                    if registro == 0:
                                        break

                                    elif registro in Mov:

                                        print('\nENTER para confirmar os dados / Digite para alterar os dados\n')

                                        resp = input(f'[{Mov[registro][1]}] | Conta de Débito:')
                                        if resp != '':
                                            Mov[registro][1] = completazero(resp)
                                        resp = input(f'[{Mov[registro][2]}] | Dígito: ')
                                        if resp != '':
                                            Mov[registro][2] = resp
                                        resp = input(f'[{Mov[registro][3]}] | Conta de Crédito: ')
                                        if resp != '':
                                            Mov[registro][3] = completazero(resp)
                                        resp = input(f'[{Mov[registro][4]}] | Dígito:')
                                        if resp != '':
                                            Mov[registro][4] = resp
                                        resp = input(f'[{Mov[registro][6]}] | Valor: ')
                                        if resp != '':
                                            Mov[registro][6] = float(resp)

                                retorno()
                                break

                    except NameError:
                        print('Não há movimentação em contas')
                        retorno()
                        break

        elif opcao == 'x':

            while True:
                mensagem('EXPORTAR DADOS')
                resp = input('Deseja exportar as contas cadastradas? [S/N] ').lower()
                if resp == 's':
                    nome_arq = input('Digite o nome do arquivo:')
                    matriz = transformatriz_contas(Contas)
                    matriz = export_contas(matriz,nome_arq)
                  
                else:
                    resp = input('Deseja exportar as movimentações feitas? [S/N] ').lower()
                    if resp =='n':
                        retorno()
                        break
                    if resp == 's' and movimentacaoCadastrada == True:
                        nome_arq = input('Digite o nome do arquivo:')
                        matriz = transformatriz_mov(Mov)
                        matriz = export_mov(matriz,nome_arq)

                        retorno()
                        break
                    

                    else:
                        mensagem('NÃO FOI POSSÍVEL REALIZAR A OPERAÇÃO: SEM MOVIMENTAÇÕES CADASTRADAS')
                        retorno()
                        break
       

                resp = input('Deseja exportar as movimentações feitas? [S/N] ').lower()
                if resp =='n':
                    retorno()
                    break
                if resp == 's' and movimentacaoCadastrada == True:
                    nome_arq = input('Digite o nome do arquivo:')
                    matriz = transformatriz_mov(Mov)
                    matriz = export_mov(matriz,nome_arq)
                    retorno()
                    break

                else:
                    mensagem('NÃO FOI POSSÍVEL REALIZAR A OPERAÇÃO:\nSEM MOVIMENTAÇÕES CADASTRADAS')
                    retorno()
                    break

        if opcao == 'b':
            data = date.today()
            print(f'''
                        DEMONSTRATIVO DE RECEITAS E DESPESAS
                        ------------------------------------

Referência: {data.month}/{data.year}
Data da emissão : {data.day}/{data.month}/{data.year}
{"-"*71}                                                         
Contas                                                              R$
{"-"*71} ''')

            Conta_ordenada = ordenaConta(Contas)
            for k, v in Conta_ordenada.items():
                k = completazero(k)
                i = obterContaCurta(k)
                desc = v[0]
                valor = v[1]
                tam_s = 30
                i += ' ' + desc
                print(f'{i: <55s} {valor:>15.2f}')
            print(f'''
{"-"*71}
{"Total de Despesas":<25s} {"Total de Receitas":<25s}{"Saldo":>20s}
''')
            vetor_saldo = total(Contas)
            saldodeb = vetor_saldo[0]
            saldocred = vetor_saldo[1]
            saldo_final = vetor_saldo[2]
            print(f'{saldodeb:<25.2f} {saldocred:<25.2f}{saldo_final:>20.2f}')
            print()
            resp = input('ENTER PARA RETORNAR...')

        elif opcao == 'i':
            while True:
                mensagem('IMPORTAR ARQUIVO CSV')
                resp = input('Deseja importar contas ? [S/N] ').lower()
                if resp == 's':
                    nome_arq = input('Digite o nome do arquivo:')
                    import_Contas = import_contas(nome_arq)
                    checagem_arquivo_Contas(import_Contas,Contas)
                    if import_Contas[1] == True:
                        contaCadastrada = True

                else:
                    resp = input('Deseja importar movimentações ? [S/N] ').lower()
                    if resp == 's':
                        nome_arq = input('Digite o nome do arquivo:')
                        import_Mov = import_mov(nome_arq)
                        checagem_arquivo_mov(import_Mov,Mov)
                        if import_Mov[1] == True:
                            movimentacaoCadastrada = True
                        retorno()
                        break
                    else:
                        retorno()
                        break
                    
                resp = input('Deseja importar movimentações ? [S/N] ').lower()
                if resp =='s':
                    nome_arq = input('Digite o nome do arquivo:')
                    import_Mov = import_mov(nome_arq)
                    checagem_arquivo_mov(import_Mov,Mov)
                    if import_Mov[1] == True:
                        movimentacaoCadastrada = True
                    retorno()
                    break

                else:
                    retorno()
                    break
    if contaCadastrada == False and (contaCadastrada==False and opcao!='c' and opcao!='i' and opcao!='s'):
            print()
            mensagem('NÃO FOI POSSÍVEL REALIZAR A OPERAÇÃO:\nSEM CONTAS CADASTRADAS')
            print()
            print()     
            retorno()

