'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Primeira Lista de Exercicios - Tipos Numéricos
Março/2022.
'''

#Exercício 2) Faça um programa que recebe a base e a altura do triângulo e imprima a área dele

print(f"\n{30*'-'}\nUtilize sempre a mesma unidade de medida (u.m.) !")
base = float(input("Insira o valor da BASE do triângulo: "))
altura = float(input("Insira o valor da ALTURA do triângulo: "))

area = (base*altura) / 2

print(f"A área do triângulo com os valores de base {base} u.m. e altura {altura} u.m. é: {area} u.a. (unidade de área)")