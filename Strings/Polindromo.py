'''
Implemente a função palindromo(palavra). Um palíndromo é uma cadeia de caracteres que pode ser
lida de frente para trás e de trás para frente. Exemplos: ‘Somos’, ‘1234321’.

O parâmetro palavra é uma string. A função deverá retornar True se palavra for um palíndromo, ou
False, caso contrário.

Observe que a string palavra pode ter um número par ou ímpar de caracteres. Observe também que as
mesmas letras maiúsculas e minúsculas devem ser consideradas como letras iguais, i.e., ‘S’ é igual a ‘s’.

'''

def polindromo(frase):
    frase = frase.strip().upper()
    termos = frase.split()
    junto = ''.join(termos)
    tras_para_frente=''

    for letra in range(len(junto)-1,-1,-1):
        tras_para_frente+= junto[letra]
    if tras_para_frente == junto:
        print('True'.format(junto , tras_para_frente))
    else :
         print('False')


#teste
polindromo('Sommos')