'''
< DESAFIO: CRIANDO UM SISTEMA BANCÁRIO >
OPERAÇÕES: sacar, depositar e visualizar extrato

DESAFIO: Fomos contratados por um grande banco para desenvolver o 
seu novo sistema. Esse bacn odeseja modernizar suas operações e para 
isso escolheu a linguagem Python. Para a primeira versão do sistema 
devemos implementar apenas 3 operações: depósito, saque e extrato.

> ---------------------------------------------------------------- <
OPERAÇÃO DE DEPÓSITO
Deve ser possível depositar valores positivos para a minha conta 
bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma
não precisamos nos preocupar em identificar qual é o número da
agência e conta bancária. Todos os depósitos devem ser armazenados
em uma variável e exibidos na operação de extrato.

OPERAÇÃO DE SAQUE
O sistema deve permitir realizar 3 saques diários com limite máximo 
de R$ 500,00 por saque. Caso o suuário não tenha saldo em conta, o 
sistema deve exibir uam mensagem informando que não será possível 
sacar o dinheiro por falta de saldo. todos os saques devem ser 
armazenados em uma variável e exibidos na operação de extrato.

OPERAÇÃO DE EXTRATO
Essa operação deve listar todos os depósitos e saques realizados na 
conta. No fim da lsitagem deve ser exibido o saldo atual da conta. 
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, 
exemplo: 1500.45 = R$ 1500.45
'''

import os
from time import sleep
from datetime import datetime


def limparTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def adicionarExtrato(preco, operacao:str):
  # PREÇO
  if operacao.upper() == 'SAQUE':
     preco = f'\033[91mR$ {preco:.2f}\033[0m'
  else:
     preco = f'\033[92mR$ {preco:.2f}\033[0m'

  # DATA
  data = datetime.now()
  dataAtual = f'{data.day}/{data.month}/{data.year}'
  
  # INCLUSÃO NA LISTA DE EXTRATO
  operacaoAtual = f'{preco} - {usuarioAtual.upper()} - {dataAtual} - {operacao}'
  extratoBancario.append(operacaoAtual)

def mensagemErro(texto, tempo, operacao):
  if operacao == 'DEPÓSITO':
      print(f'\nNão foi possível realizar o depósito!\n{texto}')
  else:
      print(f'\nNão foi possível realizar o saque!\n{texto}')
  sleep(tempo)

usuarioAtual = ''

while usuarioAtual == '':
  limparTerminal()
  usuarioAtual = input("Digite seu nome completo: ").title()

saldoBancario = 0
extratoBancario = []
quantidadeSaque = 0
LIMITEDESAQUES = 3

while True:
    try:
      limparTerminal()
      opcoesSistema = int(input(f'< SISTEMA BANCÁRIO >\nSaldo atual: R$ {saldoBancario:.2f}\n\n[1] Depósito\n[2] Saque\n[3] Extrato\n[4] SAIR\n\nOpção: '))
      


      if opcoesSistema == 1: # DEPÓSITO
        limparTerminal()
        opcoesSistemaDeposito = int(input(f'< DEPÓSITO BANCÁRIO >\nSaldo atual: R$ {saldoBancario:.2f}\n\n[1] Depositar\n[2] Voltar\n\nOpção: '))
        
        if opcoesSistemaDeposito == 1:
          depositoNovo = float(input('Depósito: R$ ').replace(',', '.'))
          if depositoNovo < 0:
              mensagemErro('O valor inserido está negativo', 3, "DEPÓSITO")
          else:
              saldoBancario += depositoNovo
              adicionarExtrato(depositoNovo, "DEPÓSITO")
          
        elif opcoesSistemaDeposito == 2: # SAIR
          continue
        
        

      elif opcoesSistema == 2: # SAQUE
        limparTerminal()
        if quantidadeSaque < LIMITEDESAQUES:
          opcoesSistemaSaque = int(input(f'< SAQUE BANCÁRIO >\nSaldo atual: R$ {saldoBancario:.2f}\n\n[1] Saque\n[2] Voltar\n\nOpção: '))

          if opcoesSistemaSaque == 1:
            saqueNovo = float(input('Saque: R$ ').replace(',', '.'))

            if saqueNovo > 0:
              if saqueNovo <= saldoBancario:
                if saqueNovo <= 500.0: 
                  saldoBancario -= saqueNovo
                  quantidadeSaque += 1
                  adicionarExtrato(saqueNovo, "SAQUE")
                else:
                  mensagemErro('Limite máximo por saque: R$ 500.00', 3, "SAQUE")
              else:
                mensagemErro('Preço a ser sacado maior do que o saldo!', 3, "SAQUE")
            else:
              mensagemErro('O valor inserido está negativo!', 3, "SAQUE")
          elif opcoesSistemaSaque == 2:
            continue
        else:
          mensagemErro('Limite diário de saques: 3', 5, "SAQUE")



      elif opcoesSistema == 3: # EXTRATO
        limparTerminal()

        print(f'< EXTRATO BANCÁRIO >\nSaldo atual: R$ {saldoBancario:.2f}\n')
        
        for linha in extratoBancario:
            print(linha)
        
        opcaoSair = input('\nClique no [ENTER] para voltar')
        if opcaoSair == '':
            continue


      elif opcoesSistema == 4: # SAIR
          break
      
    except:
       continue
    


