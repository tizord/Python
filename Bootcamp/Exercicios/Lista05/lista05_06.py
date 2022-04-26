'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Quinta Lista de Exercicios - laço de repetição
Abril/2022.
'''

# Exercício 6) Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que calcule o valor de H com N termos.

n = int(input("Insira a quantidade de termos que deseja somar: "))
h = 0

for n in range(1,n+1):
    print(1/n)
    h += (1/n)

print(f'O valor da soma dos {n} elementos é: H = {h}')
