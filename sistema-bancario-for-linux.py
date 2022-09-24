# Sistema bancário v.1 - windows

# Parte 01 - Importações
from os import system

# Parte 02 - Estruturas de texto
menu = '''
---------------------------------

        Escolha uma opção

---------------------------------

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Sair

---------------------------------

=> '''
deposito = '''
---------------------------------

             Depósito

---------------------------------

=> R$ '''
saque = '''
---------------------------------

              Saque

---------------------------------

=> R$ '''
invalido = '''
---------------------------------

       Você não pode sacar

---------------------------------
'''
movimentacao = '''
---------------------------------

        Sem movimentações

---------------------------------
'''
extrato = '''
---------------------------------

             Extrato

---------------------------------
'''
extrato_deposito = '''
    Entradas:
'''
extrato_saque = '''
    Saídas:
'''

# Parte 03 - Declaração de variáveis importantes
saldo = 0.0
limite = 500
LIMITE_SAQUES = 3
numero_saques = 0
validar_extrato = extrato_deposito + extrato_saque
limpar = 'clear'
pausar = 'read -p "Precione uma tecla para continuar..."'


# Parte 05 - Sistema do banco
while True:
    # Escolher opção
    system(limpar)
    opcao = int(input(menu))

    # Opção de depósito
    if opcao == 1:
        condicao = 'S'
        while condicao == 'S':
            valor = 0
            # Validação do valor do depósito
            while valor <= 0:
                system(limpar)
                valor = float(input(deposito)) 
                if valor <= 0:
                    continue
            # Atualização do saldo e extrato
            saldo += valor
            extrato_deposito += f'\t\tR$ {valor:.2f}\n'
            # Condição de saída  
            condicao = input('[S] Depositar outro valor: ').strip().upper()     

    # Opção de saque
    elif opcao == 2:

        # Tentar sacar sem valor ou atingindo o limite de saques diários
        if LIMITE_SAQUES == numero_saques or saldo == 0:
            system(limpar)
            print(invalido)
            system(pausar)
            continue

        # Atualizações de saque
        condicao = 'S'
        while condicao == 'S':
            valor = 0
            # Validação do saque
            while valor == 0 or valor > 500 or valor > saldo:
                system(limpar)
                valor = abs(float(input(saque)))
                if valor == 0 or valor > 500 or valor > saldo:
                    continue
            
            # Atualização do saldo, extrato e número de saques
            numero_saques += 1
            saldo -= valor
            extrato_saque += f'\t\tR$ {valor:.2f}\n'

            # Impressão de cédulas 

            # Cédulas de 50
            if valor > 50:
                quantidade = int(valor//50)
                valor -= quantidade*50
                print(f'Notas de 50: {quantidade}')
            #Cédulas de 20
            if valor > 20:
                quantidade = int(valor//20)
                valor -= quantidade*20
                print(f'Notas de 20: {quantidade}')
            #Cédulas de 10
            if valor > 10:
                quantidade = int(valor//10)
                valor -= quantidade*10
                print(f'Notas de 10: {quantidade}')
            #Cédulas de 1
            if valor > 1:
                quantidade = int(valor//1)
                valor -= quantidade*1
                print(f'Notas de 1: {quantidade}')

            # Força a saída
            if numero_saques == LIMITE_SAQUES or saldo == 0:
                condicao = 'N'
                print('\nVocê não pode mais fazer saques!\n')
                system(pausar)
                continue

            # Condição de saída  
            condicao = input('\n[S] Sacar outro valor: ').strip().upper()
    
    # Opção de extrato
    elif opcao == 3:
        system(limpar)
        # Validando extrato
        if extrato_deposito + extrato_saque == validar_extrato:
            print(movimentacao)
            print()
            system(pausar)
            continue

        # Exibindo o extrato
        print(extrato,end='')
        print(f'\033[32m{extrato_deposito}\033[m',end='') # Entradas na cor verde
        print(f'\033[31m{extrato_saque}\033[m',end='') # Saídas na cor vermelha
        print(f'''
---------------------------------
    Saldo:      R$ {saldo:.2f}
---------------------------------
''')
        system(pausar)

    # Sair
    elif opcao == 4:
        break
