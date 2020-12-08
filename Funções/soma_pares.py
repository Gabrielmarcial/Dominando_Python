'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia( ) e somaPar( ). 
A primeira função vai sortear 5 números e 
vai colocá-los dentro da lista e a segunda função vai mostrar 
a soma entre todos os valores pares sorteados pela função anterior.

 '''


from random import randint 

def sorteia(lista):
  print('Os numeros sorteados foram  ')
  for cont in range(0,5):
    n = randint(1,10)
    lista.append(n)
    print(f'{n}', end = ' ')
  print('pronto!!')

def somapar(lista):
  soma = 0 
  for c in lista: 
    if c %2 == 0:
      soma += c
  print(f' a soma dos pares é  {soma }') 




num=list()
sorteia(num)
somapar(num)