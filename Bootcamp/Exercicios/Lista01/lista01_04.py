'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Primeira Lista de Exercicios - Tipos Numéricos
Março/2022.
'''

#Exercício 4 - Faça um programa que receba peso (kg) e altura (m) e calcule o IMC

print(f"\n{30*'-'}\n")
peso = float(input("Insira seu peso (kg): "))
altura = float(input("Insira sua altura (m): "))

imc = peso / altura**2
print(f"O IMC de uma pessoa com {peso} kg e {altura} m é: {imc:.3f}")

