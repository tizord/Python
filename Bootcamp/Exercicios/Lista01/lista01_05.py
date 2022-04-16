'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Primeira Lista de Exercicios - Tipos Numéricos
Março/2022.
'''

#Exercício 5 - Escreva um programa que leia um número de 4 digitos e retorne a soma desses digitos

print(f"\n{30*'-'}\n")
numero = int(input("Insira um número de 4 dígitos (numero inteiro): "))

verificatamanho = numero//1000

if (verificatamanho < 1 or verificatamanho > 9):
    print("Esse número não tem 4 dígitos! ")
else:
    milhar = numero // 1000
    resto = numero % 1000
    centena = resto // 100
    resto = resto % 100
    dezena = resto // 10
    resto = resto - (dezena*10)
    unidade = resto

    total = milhar + centena + dezena + resto
    print(f"A soma dos dígitos do número {numero} é: {total}")