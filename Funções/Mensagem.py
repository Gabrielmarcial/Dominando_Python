''' 
Faça um programa que tenha uma função chamada escreva(), que 
receba um texto qualquer como parâmetro e 
mostre uma mensagem com tamanho adaptável.'''

def escreva(msg): 
    
    print('_-'*len(msg))
    print(f' {msg}  ')
    print('_-'*len(msg))


