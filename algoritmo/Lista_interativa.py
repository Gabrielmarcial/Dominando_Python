'''Escreva um programa para criar uma lista de tuplas contendo quatro itens relativos a uma mesma pessoa:
(nome, email, dia nascimento, mês nascimento).Implemente funções para fazer um 
cadastro: incluir(), consultar(), consultar_aniversariante(), listar()
O programa deverá implementar um laço principal na função main(), apresentando as opções disponíveis,
bem como uma opção para encerrar a execução. Implemente um menu de opções em forma de uma função.
Use um arquivo texto para salvar os dados. Esse arquivo deverá ser lido a cada vez que o programa 
começar e deverá ser gravado a cada vez que o programa terminar.'''

#-----------Resolução----------------#

def main():
  
  
  print("==="*30)
  print('SEJA BEM VINDO')

  print("""FUNÇÕES DISPONIVEIS:
            incluir(0) ---> Para adicionar dados
            listar(1)  ---> Para listar todos os dados disponiveis
            consultar(2) ---> Para Consultar uma pessoa em especifico
            consultar_aniversariante(3) ---> Para consultar os aniversariantes do mês
            sair(4) ---> Encerrar """)
  print("==="*30)

  
  dados = []

  def incluir():
    nome = str(input('Nome:'))
    email = str(input('Email:'))
    dia_nasc = int(input('Dia do nasciemento:'))
    mes_nasc = int(input('Mês do nascimento:'))
    dados_pessoa = nome,email,dia_nasc,mes_nasc
    dados.append(dados_pessoa)  


  def consultar():
    n = str(input('Qual nome deseja consultar:'))
    for i in range(0,len(dados)):
      if n == dados[i][0]:
        print('====='*40)
        print('Nome:{}'.format(dados[i][0]))
        print('Email:{}'.format(dados[i][1]))
        print('Dia do nasciemento:{}'.format(dados[i][2]))
        print('Mês do nascimento:{}'.format(dados[i][3]))
        print('====='*40)
  

  def listar():
    print('======'*40)
    print('Todos os dados')
    print('======'*40)
    for c in range(0,len(dados)):
      print('Nome:{}'.format(dados[c][0]))
      print('Email:{}'.format(dados[c][1]))
      print('Dia do nasciemento:{}'.format(dados[c][2]))
      print('Mês do nascimento:{}'.format(dados[c][3]))
      print('====='*40)
  
  def consultar_aniversariante():
    d = int(input('Dia atual:'))
    m = int(input('Mês :'))
    v = []
    for j in range(0,len(dados)):
      if dados[j][2] == d and dados[j][3] == m :
        v.append(dados[j][0])
      
    if len(v)>0: 
      print('Aniversariantes do Mês')
      for aniversariantes in range(0,len(v)):
          print(v[aniversariantes])
    else : 
      print('Não tem aniversariantes')


  s = 1
  def sair():
    arquivo = open("texto.txt", "a")
    arquivo.write('===============\n')
    arquivo.write('Todos os dados\n')
    arquivo.write('===============\n')
    for c in range(0,len(dados)):
      arquivo.write('Nome:{}\n'.format(dados[c][0]))
      arquivo.write('Email:{}\n'.format(dados[c][1]))
      arquivo.write('Dia do nasciemento:{}\n'.format(dados[c][2]))
      arquivo.write('Mês do nascimento:{}\n'.format(dados[c][3]))
      arquivo.write('===============\n')

    arquivo = open("texto.txt", "a")

    print('Obrigado por usar nossos serviços'.upper())
    

  while s != 0 : 
    d =  int(input('OQUE deseja ?:'.upper()))
    print('====='*40)

    if d == 0 : 
      incluir()
    
    if d == 1 : 
      listar()
 
    if d == 2 : 
      consultar()
  
    if d == 3 : 
      consultar_aniversariante()

    if d == 4: 
      sair()
      break
  
  
main()