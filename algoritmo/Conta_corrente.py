'''Escreva um programa que crie um classe para representar uma conta corrente de um banco
 A classe terá um número e um saldo. Defina métodos para depositar e sacar. 
 Em casos de saques, caso o valor seja maior que o saldo, gere uma exceção ValueError. 
 No método construtor, saldo terá valor default zero. 
 Crie um objeto conta e faça alguns depósitos e saques e informe o saldo a cada operação.'''

 #-----------Resolução----------------#

class contacorrente:

  deposito_total = 0
  saque_total = 0

  def depositar(self,entrada):
     self.entrada = entrada
     self.__class__.deposito_total += entrada
     print(f'foi depositado : R$ {entrada}') 
     print('----'*10)

  
  def sacar(self,saida):
      self.saida = saida
      saldo = self.__class__.deposito_total-self.__class__.saque_total
      if saida > saldo: 
        try:
            x = int('valorerrado')
        except ValueError:
          print(f'Valor de R$ {saida} insuficiente para saque,por favor escolha um valor disponivel')
          print(f'saldo disponivel para saque : R$ {saldo}')
          print('----'*10)
      else:
        self.__class__.saque_total += saida
        print(f'foi sacado : R$ {saida}')
        print('----'*10) 

  def saldo(self):
    saldo = self.__class__.deposito_total-self.__class__.saque_total 
    print(f'Seu saldo atual é : R$ {saldo}')
    print('----'*10)
  
  
conta = contacorrente()
conta.saldo()
conta.depositar(12)
conta.depositar(4)
conta.sacar(5)
conta.sacar(13)
conta.sacar(4)
conta.saldo()
