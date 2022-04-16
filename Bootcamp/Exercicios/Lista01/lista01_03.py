'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Primeira Lista de Exercicios - Tipos Numéricos
Março/2022.
'''
#Exercício 3) Faça um programa que receba os 3 lados de um triangulo e calcule sua área

from math import sqrt

print(f"\n{30*'-'}\n")
l1 = float(input("Insira o valor do primeiro lado do triângulo: "))
l2 = float(input("Insira o valor do segundo lado do triângulo: "))
l3 = float(input("Insira o valor do terceiro lado do triângulo: "))

l = (l1 + l2 + l3) / 2
arealinha = sqrt(l*(l-l1)*(l-l2)*(l-l3))

print(f"A área do triangulo cujos lados são {l1, l2, l3} é {arealinha}")
