'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Quarta Lista de Exercicios - Condicionais
Abril/2022.
'''
# Exercício 1) Escreva um programa que diga se um número dado pelo usuário é par ou ímpar

numero = int(input("Insira um número INTEIRO: "))

resto = numero % 2

if resto == 0:
    print(f'O número {numero} é PAR')

else:
    print(f'O número {numero} é ÍMPAR')