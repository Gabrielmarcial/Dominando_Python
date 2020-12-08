''' Crie um programa que implemente a Regra de Cramer para um sistema de 3 equações e 3 incógnitas.

1. O programa deve ler uma matriz {aij} e um vetor {di} de coeficientes, e deve conter uma função
Cramer(matriz, vetor), que calcula as raízes do sistema e retorna a solução na forma de um
vetor: [x, y, z].

2. Caso o sistema seja consistente e indeterminado (infinitas soluções), a função Cramer(matriz,
vetor) deve retornar [0]. Caso o sistema seja inconsistente (sem solução), a função
Cramer(matriz, vetor) deve retornar [1].

3. A função Cramer(matriz, vetor) deve chamar a função det(matriz), que retorna o valor do
determinante da matriz.

4. O programa principal deve, depois de chamada a função Cramer(matriz, vetor), apresentar ao
usuário as raízes do sistema, ou indicar se ele é consistente e indeterminado, ou inconsistente.
'''

# determinante 
def det(matriz):
    Detmatriz = (matriz[0][0] * matriz[1][1] * matriz[2][2])
    Detmatriz = Detmatriz + (matriz[0][1] * matriz[1][2] * matriz[2][0])
    Detmatriz = Detmatriz + (matriz[0][2] * matriz[1][0] * matriz[2][1])
    Detmatriz = Detmatriz - (matriz[2][0] * matriz[1][1] * matriz[0][2])
    Detmatriz = Detmatriz - (matriz[2][1] * matriz[1][2] * matriz[0][0])
    Detmatriz = Detmatriz - (matriz[2][2] * matriz[1][0] * matriz[0][1])
    return Detmatriz
    
# solução do sistema
import copy
def cramer(matriz,vetor):
  # achando o X da E.Q 
  matriz_x = copy.deepcopy(matriz)
  matriz_x[0][0] = vetor[0]
  matriz_x[1][0] = vetor[1]
  matriz_x[2][0] = vetor[2]
  x = det(matriz_x)/det(matriz)

  # achando o y da E.Q 
  matriz_y = copy.deepcopy(matriz)
  matriz_y[0][1] = vetor[0]
  matriz_y[1][1] = vetor[1]
  matriz_y[2][1] = vetor[2]
  y = det(matriz_y)/det(matriz)

  # achando o z da E.Q 
  matriz_z = copy.deepcopy(matriz)
  matriz_z[0][2] = vetor[0]
  matriz_z[1][2] = vetor[1]
  matriz_z[2][2] = vetor[2]
  z = det(matriz_z)/det(matriz)
  

  print(f'As raizes do sistema são [{x} , {y} , {z} ]')

  if det(matriz)!=0 : 
    print('sistema consistente e determinado.')
  
  if det(matriz)==0 and det(matriz_x) == 0 and det(matriz_y)==0 and det(matriz_z) == 0: 
    print('[0]')
    print('sistema consistente e indeterminado.')

  if det(matriz) == 0  and det(matriz_x) != 0 and det(matriz_y)!=0 and det(matriz_z) != 0: 
    print('[1]')
    print('sistema inconsistente.')


cramer([[4,-1,1],[1,2,-1],[1,0,-1]],[-1,-2,-5])