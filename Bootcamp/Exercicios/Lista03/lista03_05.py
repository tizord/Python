'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Terceira Lista de Exercicios - Sets
Abril/2022.
'''

# Exercício 5) Faça um programa que encontre as notas mínimas e máximas de um dicionário, e imprima-os na 
# tela com as suas respectivas chaves.

dicionario_notas = dict([('Theodoro', 58), ('Márcia', 69), ('Júnior', 73), ('João', 82)])

notas = list(dicionario_notas.values())
nota_max = max(notas)
nota_min = min(notas)

for chave in dicionario_notas.keys():
    if dicionario_notas[chave] == nota_max:
        print(f'Nota máxima -> {chave} : {nota_max}')
    
for chave in dicionario_notas.keys():
    if dicionario_notas[chave] == nota_min:
        print(f'Nota mínima -> {chave} : {nota_min}')