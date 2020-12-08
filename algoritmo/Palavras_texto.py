'''  
Escreva um programa para ler um arquivo texto fornecido (“Receita de Ano Novo.txt”) e fazer a
contagem de espaços, de cada letra maiúscula e de cada letra minúscula, imprimir os valores
encontrados e identificar a letra (maiúscula ou minúscula) com maior número de ocorrências.
Funções: o programa terá duas funções:

a) Uma para abrir o arquivo, ler o texto e fechar o arquivo. Essa função deverá retornar o texto
lido.

b) Outra função para processar o texto. Essa função receberá o texto como argumento.

c) Essas duas funções deverão ser chamadas a partir da função principal ( main() ).
Importante: na avaliação da solução apresentada, será considerada a estrutura usada para construir o
programa.

Observações:

a) O texto contido no arquivo não possui letras acentuadas nem o caractere ‘ç’, isto é, todos os
caracteres possuem códigos ASCII até 127.

b) O texto contido no arquivo possui alguns sinais de pontuação.

c) Os códigos ASCII na faixa 0 a 31 são caracteres de controle e não devem ser considerados (por
exemplo, caractere de nova linha e marcas de tabulação).
Códigos ASCII:
‘A’ – ’Z’: 65 – 90;
‘a’ – ’z’: 97 – 122;
‘ ’ : 32 (espaço em branco)
Lembre-se que você dispõe das funções ord(<caractere>), que retorna o código ASCII de <caractere>,
e chr(<código>), que retorna o caractere que tem <código> ASCII. '''

def main():
    # Lendo o arquivo letra (a)
    def read():
        arquivo = open("Receita de Ano Novo.txt", "r")# aqui vc deve colocar o caminho referente ao arquivo 
        a = arquivo.read()
        print(a)
        arquivo.close()

    def text():
        # abrindo o arquivo
        arquivo = open("Receita de Ano Novo.txt", "r")
        b = arquivo.readlines()

        # Verificando a quantidade de Maisculas/Minusculas/espaços
        maiuscula = 0
        maiuscula_ordem = []
        minuscula = 0
        minuscula_ordem = []
        espaco = 0

        for i in range(0, len(b)):

            for c in range(0, len(b[i])):
                ordem = int(ord(b[i][c]))

                if 65 <= ordem <= 90:
                    maiuscula = maiuscula + 1
                    maiuscula_ordem.append(ordem)

                if 97 <= ordem <= 122:
                    minuscula = minuscula + 1
                    minuscula_ordem.append(ordem)

                if ordem == 32:
                    espaco = espaco + 1
        print('===' * 30)
        print(f'Temos nesse texto {maiuscula} letras maisculas ')
        print(f'Temos nesse texto {minuscula} letras minusculas ')
        print(f'Temos nesse texto {espaco} espaços ')

        # Letra com a maior ocorrencia

        maiuscula_ocorrencia = {}
        for element in maiuscula_ordem:
            maiuscula_ocorrencia[chr(element)] = maiuscula_ordem.count(element)
        print('--------Letras maisculas-------- ')
        for l in maiuscula_ocorrencia:
            print(f'A letra <{l}> apareceu :{maiuscula_ocorrencia[l]} vezes.')

        minuscula_ocorrencia = {}
        for element in minuscula_ordem:
            minuscula_ocorrencia[chr(element)] = minuscula_ordem.count(element)

        print('------Letras minusculas------')
        for l in minuscula_ocorrencia:
            print(f'A letra <{l}> apareceu :{minuscula_ocorrencia[l]} vezes.')

        maior_maiuscula = max(maiuscula_ocorrencia.items(), key=lambda x: x[1])
        maior_minuscula = max(minuscula_ocorrencia.items(), key=lambda x: x[1])

        maior_ocorrencia = ()
        if maior_maiuscula[1] > maior_maiuscula[1]:
            maior_ocorrencia = maior_maiuscula
        else:
            maior_ocorrencia = maior_minuscula
        print('------Maior ocorrência------')
        print(f'A letra que apareceu mais foi a letra <{maior_ocorrencia[0]}> com {maior_ocorrencia[1]} ocorrências ')
        print('===' * 30)

    read()
    text()


main()