'''
01. Donuts
Dado um contador inteiro do numero de donuts, retorne uma string com o formato 'Number of donuts:
'onde é o numero recebido. Entretanto, se o contador for 10 ou mais, use a palavra 'many' ao invés do contador. 
Exemplo: donuts(5) retorna 'Number of donuts: 5' e donuts(23) retorna 'Number of donuts: many'
'''

def donuts(count):
    if count<10:
      result= str(f'Number of donuts: {count}')  
    else: 
      result= 'Number of donuts: many'
    return result