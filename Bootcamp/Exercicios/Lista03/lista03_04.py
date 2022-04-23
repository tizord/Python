'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Terceira Lista de Exercicios - Sets
Abril/2022.
'''

# Exercício 4) Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de 
# dicionário.

dicionario_palavras = dict(zip([1, 2, 3, 4, 5], ['Vermelho', 'Azul', 'Marrom', 'Laranja']))

for _ in dicionario_palavras.keys():
    tamanho = len(dicionario_palavras[_])
    dicionario_palavras[_] = tamanho

print(dicionario_palavras)