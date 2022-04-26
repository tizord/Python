'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Quarta Lista de Exercicios - Condicionais
Abril/2022.
'''

# Exercício 2) Escreva um programa que receba dois números e imprima na tela se o primeiro é divisível pelo segundo.

numero1 = int(input("Insira o primeiro número: "))
numero2 = int(input("Insira o segundo número: "))

resto = numero1 % numero2

if resto == 0:
    print(f'O número {numero1} é divisível pelo número {numero2}')

else:
    print(f'O número {numero1} NÃO é divisível pelo número {numero2}')