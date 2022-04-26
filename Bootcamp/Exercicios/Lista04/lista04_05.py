'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Quarta Lista de Exercicios - Condicionais
Abril/2022.
'''

# Exercício 5) Escreva um programa que receba uma string e diga se ela tem o formato de uma placa veicular brasileira 
# (no formato antigo) com três letras, um traço e quatro números

verifica_placa = input('Insira uma placa veicular brasileiro: ')

tamanho_string = len(verifica_placa)
letras_string = verifica_placa[:3]
numeros_string = verifica_placa[4:]

print(f'A placa {verifica_placa} tem o formato brasileiro?')
if tamanho_string != 8:
    print(False)

if (verifica_placa[3] == '-' and letras_string.isalpha and numeros_string.isdigit() and letras_string.isupper()):
    print(True)
else:
    print(False)