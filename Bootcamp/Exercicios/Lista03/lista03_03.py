'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Terceira Lista de Exercicios - Sets
Abril/2022.
'''

#Exercício 3) Faça um programa que ordene um dicionário por seus valores.

dicionario_notas = {'Português': 77, 'Biologia': 81, 'Física': 87, 'Matemática': 91, 'História': 88, 'Geografia': 66, 'Química': 78}

dicionario_lista = list(dicionario_notas.items())
chaves_decrescentes =[]
valores_decrescentes = []

valores_decrescentes = sorted(dicionario_notas.values())

for valor in valores_decrescentes:
    for _ in range(len(valores_decrescentes)):
        if dicionario_lista[_][1] == valor:
            chaves_decrescentes.append(dicionario_lista[_][0])


dicionario_ordenado = dict(zip(chaves_decrescentes, valores_decrescentes))

print(f"O dicionário de notas:\n{dicionario_notas} \nquando ordenado pelos valores é:\n{dicionario_ordenado}")