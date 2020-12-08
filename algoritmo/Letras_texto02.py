''' 
Crie um programa que leia um arquivo texto entrada.txt e conte quantas vezes cada letra aparece no
texto dentro do arquivo.

Você pode considerar letras acentuadas como letras distintas, i.e., ‘A’ é diferente de ‘Á’, mas letras
maiúsculas e minúsculas devem ser tratadas como letras iguais, i.e., ‘A’ é igual a ‘a’.

O programa deve gravar o resultado em um arquivo saida.txt, que deve conter cada letra e o respectivo
número de ocorrências.

As letras no arquivo de saída devem ser apresentadas em ordem alfabética. Cada letra deve aparecer
em uma linha, seguida pelo número de ocorrências. O formato do arquivo deve ser parecido com:
A 13
B 28
Z 1 
'''
# Lendo o arquivo Entrada.txt
arquivo = open("Entrada.txt", "r")
a = arquivo.read()
print(a)
arquivo.close()

#abrindo e trabalhando com o arquivo 
arquivo = open("Entrada.txt", "r")
b = arquivo.readlines()

# Verificando a quantidade de Maisculas/Minusculas
maiuscula = 0
maiuscula_ordem = []
minuscula = 0
minuscula_ordem = []

for i in range(0, len(b)):

  for c in range(0, len(b[i])):
       ordem = int(ord(b[i][c]))

       if 65 <= ordem <= 90:
          maiuscula = maiuscula + 1
          maiuscula_ordem.append(ordem)

       if 97 <= ordem <= 122:
            minuscula = minuscula + 1
            minuscula_ordem.append(ordem)


# Salvando com dic com suas respectivas ocorrencias 
maiuscula_ocorrencia = {}
for element in maiuscula_ordem:
    maiuscula_ocorrencia[chr(element)] = maiuscula_ordem.count(element)


minuscula_ocorrencia = {}
for element in minuscula_ordem:
    minuscula_ocorrencia[chr(element)] = minuscula_ordem.count(element)


#verificando as iguais

final = {}
for l in maiuscula_ocorrencia:
    for c in minuscula_ocorrencia:
      if ord(c) - ord(l) ==  32 :
          final[l] = maiuscula_ocorrencia[l] + minuscula_ocorrencia[c] 

# completando 
for c in minuscula_ocorrencia:
      num = 0
      for l in final:
        if l == c or l == c.upper()  :
          num = num + 1 
      if num == 0 : 
        final[c] = minuscula_ocorrencia[c]

# Salvando em um arquivo saida.txt   
saida = open("saida.txt",'a')

for letra in sorted(final):
    saida.write(f'{letra} : {final[letra]}\n')
