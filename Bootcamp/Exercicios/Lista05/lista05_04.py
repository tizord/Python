'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Quinta Lista de Exercicios - laço de repetição
Abril/2022.
'''

# Exercício 4 - Desafio) Escreva um programa que calcule o número pi com 15 aproximações.

n = int(input("Insira a quantidade de aproximações para o cálculo de pi: "))

pi_calculo = 3

print(list(range(2,n+1)))

if n == 1:
    pass
else:
    for n in range(2,n+1):
        
        termo = (-1) ** n * ( (4) / ( (2*n -2) * (2*n - 1) * (2*n) ) )
        pi_calculo += termo

print(f'O valor de pi com aproximação n = {n} é: {pi_calculo}')
