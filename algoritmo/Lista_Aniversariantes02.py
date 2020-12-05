''''Escreva um programa que crie um dicionário contendo 4 itens relativos a uma mesma pessoa, 
tendo 'Nome' como chave e os demais itens formando uma tupla: {Nome: (Email, Dia de nascimento, Mês de nascimento)}
Use números aleatórios para gerar Dia e Mês. Use a função chr(<num>), para gerar nomes aleatórios com até 10 letras. 
O email terá o formato <nome>@xyz.com.br Você deverá gerar dados para representar um grupo de 100 pessoas. 
Após criar o grupo de 100 pessoas, complete  o programa verificando se há na lista 
algum aniversariante do dia. Você poderá informar o dia e o mês atuais. 
A saída do programa será a a relação dos nomes dos aniversariantes. '''

#-----------Resolução----------------#

import random
lista = {}
nomes =[]
for c in range(0,100):
  nome = chr(random.randrange(65, 90))
  for i in range(0,random.randrange(1, 10)):
      nome = nome + chr(random.randrange(97, 122))
  email = nome+'@xyz.com.br'
  dia = random.randrange(1, 30)
  mes = random.randrange(1, 12)
  t = email,dia,mes
  lista[nome] = t
  nomes.append(nome)

print(lista)

#verificando os aniversariantes. 
d = int(input('Dia atual:'))
m = int(input('Mês :'))
v = []
for j in range(0,len(lista)):
  if lista[nomes[j]][1] == d and lista[nomes[j]][2] == m :
    v.append(nomes[j])
    print('Feliz aniversario {}'.format(nomes[j])) 


if len(v)>0: 
  print('Aniversariantes do Mês')
  for aniversariantes in range(0,len(v)):
      print(v[aniversariantes])
else : 
  print('Não tem aniversariantes')