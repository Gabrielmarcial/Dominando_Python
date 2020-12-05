'''Escreva um Programa onde vc entre com um nome e 
ele retorne a primeira letra em maiuscula e o restante em minuscula.'''


#-----------Resolução----------------#

# Primeira resolução 
n = str(input('Qual seu nome:'))
n = n.strip()
v =  [ ]

for c in range(0,len(n)):
    v.append(n[c])

for j in range(0,len(v)-1):    
    if j == 0 : 
        v[0] = v[0].upper()
        for k in range(j+1,len(v)):
            v[k] = v[k].lower()
    if v[j] == " ":
       v[j+1] = v[j+1].upper()
       
for i in range(0,len(v)): 
    print(v[i], end= " " )


# Segunda resolução 
# s = str(input('nome : '))
# s = s.strip()
# lst = [letra[0].upper() + letra[1:].lower() for letra in s.split()]
# s = " ".join(lst)
# print(s)