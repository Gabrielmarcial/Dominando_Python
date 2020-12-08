'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro 
o ano de nascimento de uma pessoa, retornando um valor literal 4
indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições. 
'''
def voto(ano):
  from datetime import date
  atual = date.today().year
  idade = atual - ano
  if idade < 16 :
    return f'com {idade} anos: NÃO VOTA.'
  elif 16 <= idade <18 or idade > 65: 
    return f'Com {ano} anos : VOTO OPCIONAL.'
  else: 
    return f' Com {ano} anos: VOTO OBRIGATORIO.'
nasc = int(input('Em que ano vc nasceu ? :'))
print(voto(nasc)) 
