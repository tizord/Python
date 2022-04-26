'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Quinta Lista de Exercicios - laço de repetição
Abril/2022.
'''

# Exercício 1) criará um programa que calcula a média de uma coleção de valores inseridos pelo usuário e 
# imprime-a na tela. O usuário digitará 0 como um valor para indicar que nenhum outro valor será fornecido. 
# Seu programa deve exibir uma mensagem de erro se o primeiro valor inserido pelo usuário for 0.

calcular_media =[]

numero = float(input('Insira um número: '))

if numero ==  0:
    print('Como o 0 é um valor de condição de parada, ele não deve entrar no cálculo da média!')

calcular_media.append(numero)

while numero != 0:
    numero = float(input('Insira mais um número: '))
    if numero != 0:
        calcular_media.append(numero)

media = sum(calcular_media) / len(calcular_media)

print(f'A média dos valores digitados {calcular_media} é {media}')