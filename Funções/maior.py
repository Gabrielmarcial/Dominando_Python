''' 
Faça um programa que tenha uma função chamada maior(), 
que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior(*num):
  cont = maior = 0 
  for valor in num : 
    print(f'{valor}', end= ' ')
    if cont == 0 :
      maior = valor
    else: 
      if valor > maior:
        maior = valor 
    cont += 1
  print (f' o maior vlor é {maior}')