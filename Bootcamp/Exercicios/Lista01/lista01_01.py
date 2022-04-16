'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Primeira Lista de Exercicios - Tipos Numéricos
Março/2022.
'''

#Exercicio 1: Faça um programa que receba dois numeros (A e B) e imprima na tela:
# 1) A Soma
# 2) A diferença B - A
# 3) O produto A.B
# 4) O quociente A/B
# 5) O resto da divisão A/B
# 5) O resultado log10(A)
# 6) A^B

a = float(input("Insira um numero (A): "))
b = float(input("Insira um numero (B): "))

#1) Soma
soma = a + b

print(f"A soma de {a} + {b} é {soma}")

#2) Diferença
diferenca = b - a

print(f"A diferença de {b} por {a} é {diferenca}")

#3) Produto
produto = a*b

print(f"O produto de {a} por {b} é {produto}")

#4) Quociente
if (a < 0 and b>0):
    alinha = a * (-1)
    quociente = alinha//b
    quociente = quociente * (-1)
    print(f"O quociente de {a} por {b} é {quociente}")
elif (b < 0 and a > 0):
    blinha = b * (-1)
    quociente = a//blinha
    quociente = quociente * (-1)
    print(f"O quociente de {a} por {b} é {quociente}")
elif ((b < 0 and a < 0) or (b > 0 and a > 0)) :
    quociente = a//b
    print(f"O quociente de {a} por {b} é {quociente}")
else:
    print(f"A divisão por de a por 0 é indeterminada")

#5) Resto
if b == 0:
    print(f"A divisão por zero não é definida (b = {b:.0f})")
else:
    resto = a%b
    print(f"O resto da divisão de {a} por {b} é {resto}")

#6) Logaritmo
from cmath import sqrt
from math import log10

if a > 0:
    logaritmo = log10(a)
    print(f"O logaritimo na base 10 de {a} é {logaritmo}")
else:
    print(f"O número {a} não possui logaritmo definido nos Reais")


#7) Potencia

potencia = a**b

print(f"A potencia  {a} elevado a {b} é {potencia}")