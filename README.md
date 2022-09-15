# Sistem Bancário

    - Sistema criado com linguagem Python.

## Divisão do programa

01. Importações

2. Estruturas de textos utilizadas dentro do programa

3. Declaração de variáveis importantes

4. Sistema do banco
   
   1. Escolher opção e limpeza da tela
   
   2. Depósito
      
      1. Validação do valor de depósito: Somente valores maiores do que 0
      
      2. Atualização do saldo da conta e extrato de depósitos
      
      3. Condição de saída: Continua depositando novos valores caso o usuário deseja
   
   3. Saque
      
      1. Condição de negar o saque: Caso o saldo seja zero ou atingir o limite de saques diários
      
      2. Saque
         
         1. Validação do saque: Valor diferente de 0, valor maior que 500 ou valor maior que o saldo
         
         2. Atualização do saldo, extrato e número de saques
         
         3. Impressão de cédulas
            
            1. Cédulas de 50
            
            2. Cédulas de 20
            
            3. Cédulas de 10
            
            4. Cédulas de 1
         
         4. Forçar não sacar mais: Caso o saldo seja zero ou atingir o limite de saques diários
         
         5. Condição de saída: Continua sacando novos valores caso o usuário deseja
   
   4. Extrato
      
      1. Validação do extrato: Caso não tenha movimentação mostra na tela
      
      2. Exibição do extrato
   
   5. Encerra o acesso
