'''
02. both_ends
Dada uma string s, retorne uma string feita com os dois primeiros e os dois ultimos caracteres da string original. 
Exemplo: 'spring' retorna 'spng'. Entretanto, se o tamanho da string for menor que 2, retorne uma string vazia.
'''

def both_ends(s):
    
    if len(s)>=2:
      result =  s[0]+s[1]+s[len(s)-2]+s[len(s)-1]
    
    else:
      result = ''
    
    return result 

    # segunda forma silplificada 
    #  return '' if len(s) < 2 else s[0:2] + s[-2:]