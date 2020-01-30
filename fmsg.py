#Funções de mensagens
import os

def retorno():
    """
Mensagem de interação com o usuário parar retornar ao MENU
    """
    from time import sleep
    sleep(1)
    print('RETORNANDO AO MENU...', end=' ')
    print()
    sleep(2.5)

def mensagem(msg):
    """
Formatação padrão de mensagens de interação básicas com o usuário:
exemplo: mensagem('CADASTRAR CONTA') - resultado =

----------------------------------------
            CADASTRAR CONTA             
----------------------------------------
    """
    print('-' * 40)
    print(f'{msg:^40}')
    print('-' * 40)


def menu():
    """
Mensagem mostrando o menu
    """
    print('''\nSistema de Gerenciamento de Receitas e Despesas 

  (c) Cadastrar contas
  (d) Digitar movimento financeiro
  (a) Crítica do movimento financeiro
  (p) Processar movimento
  (i) Importar arquivo CSV
    > contas
    > movimentação financeira
  (x) Exportar dados
    > contas
    > movimentação financeira
  (b) Imprimir balancete
  (s) Sair''')

def cls():
    print('\n'*80)
