'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Terceira Lista de Exercicios - Sets
Abril/2022.
'''

#Exercício 3) Faça um programa que ordene um dicionário por seus valores.

dicionario_notas = {'Português': '77', 'Biologia': '81', 'Física': '87', 'Matemática': '91', 'História': '88', 'Geografia': '66'}

valores_decrescentes = []

for _ in dicionario_notas.values():
    valores_decrescentes.append(_)

print(valores_decrescentes)