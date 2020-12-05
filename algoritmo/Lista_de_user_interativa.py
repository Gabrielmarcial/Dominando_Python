''' Escrever um programa para criar uma fila, representada por uma lista, 
e apresentar ao usuário as opções de inserir, remover, obter a frente da fila e 
visualizar todo o conteúdo da fila, bem como uma opção para encerramento do programa. 
Utilize números inteiros como elementos para serem armazenados na fila.'''

#-----------Resolução----------------#

f = []
a = 1 

while a != 0: 
  print("==="*30)
  print('SEJA BEM VINDO')
  print("""
        [1] - inserir um valor
        [2] - remover um valor 
        [3] - Primeiros valores 
        [4] - Visualizar todos os valores 
        [5] - Encerrar     
     """)
  print("==="*30)
  n = int(input('O que deseja:'))
  
  if n == 1: 
    valor = float(input('Entre com um valor:'))
    f.append(valor)

  if n ==2 :
    r = int(input('Qual valor deseja retirar:'))
    f.remove(r)

  if n == 3 :
    for c in range(0,2):
      print(f'valor n°{c} : {f[c]}') 

  if n==4: 
    print('=====FILA=====')
    for c in range(0,len(f)):
      print(f'valor n°{c} é {f[c]}') 


  if n == 5: 
     break 