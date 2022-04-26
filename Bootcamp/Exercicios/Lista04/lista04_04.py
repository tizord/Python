'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Quarta Lista de Exercicios - Condicionais
Abril/2022.
'''

# Exercício 4) Faça um programa que impima na tela se umd ado ano é bissexto ou não de acordo com as regras na
# ordem abaixo:
# 1- Um ano que é divisível por 400 é bissexto
# 2 - Dos anos que não entram na regra 1, se o ano for divisível por 100 então NÃO é bissexto
# 3 - Dos anos que não entram na regra 2, se o ano for divisível por 4, então ele é um ano bissexto
# 4 - Todos os outros anos não são bissextos

verifica_ano = int(input("Insira um ano para verificar se ele é bissexto: "))

resto_div_400 = verifica_ano % 400
resto_div_100 = verifica_ano % 100
resto_div_4 = verifica_ano % 4

if resto_div_400 == 0:
    print(f'O ano {verifica_ano} é bissexto!')

elif resto_div_100 == 0:
    print(f'O ano {verifica_ano} NÃO é bissexto.')

elif resto_div_4 == 0:
    print(f'O ano {verifica_ano} é bissexto! ')

else:
    print(f'O ano {verifica_ano} não é bissexto.')
