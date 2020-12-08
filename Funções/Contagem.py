''' 
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
início, fim e passo. Seu programa tem que realizar três contagens através 
da função criada:

a) de 1 até 10, de 1 em 1

b) de 10 até 0, de 2 em 2

c) uma contagem personalizada
'''

def contagem(i,f,p) :
  if p < 0 :
    p  = p*-1
  if p ==0 :
    p = 1
  print(f'contagem de {i} até {f} de {p} em {p}')
  if i < f:
    cont = i
    while cont <= f: 
      print(f'{cont}', end=' ')
      cont += p 
    print('FIM!')
  else: 
    cont = i 
    while cont >=f: 
      print(f'{cont}', end=' ')
      cont -= p
    print('FIM!') 
 