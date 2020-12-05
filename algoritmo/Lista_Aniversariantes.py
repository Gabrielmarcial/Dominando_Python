'''Gerar tuplas contendo 4 itens relativos a uma mesma pessoa: Nome; Email; Dia de nascimento; Mês de nascimento.
 Use uma tupla para cada pessoa e armazene-as em uma lista com capacidade para 100 pessoas. 
 Utilize números aleatórios para gerar dia e mês de nascimento. Usando a função chr(<num>), 
 gere nomes aleatórios com até 10 letras. Use esse nome para construir o endereço eletrônico (email) 
 com o formato <nome>@xyz.com.br. Após criar a lista de 100 pessoas, 
 complete  o programa verificando se há na lista algum aniversariante do dia. 
 Você poderá informar o dia e o mês atuais. A saída do programa será a lista de nomes dos aniversariantes.'''

#-----------Resolução----------------#

import random
lista = []
for c in range(0,100):
  nome = chr(random.randrange(65, 90))
  for i in range(0,random.randrange(1, 10)):
      nome = nome + chr(random.randrange(97, 122))
  email = nome+'@xyz.com.br'
  dia = random.randrange(1, 30)
  mes = random.randrange(1, 12)
  t = nome,email,dia,mes
  lista.append(t)

#verificando os aniversariantes. 
d = int(input('Dia atual:'))
m = int(input('Mês :'))
v = []
for j in range(0,len(lista)):
  if lista[j][2] == d and lista[j][3] == m :
    v.append(lista[j][0])
    print('Feliz aniversario {}'.format(lista[j][0])) 


if len(v)>0: 
  print('Aniversariantes do Mês')
  for aniversariantes in range(0,len(v)):
      print(v[aniversariantes])
else : 
  print('Não tem aniversariantes')