'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Segunda Lista de Exercicios - Listas
Março/2022.
'''

#Exercício 6) Faça um programa que remova strings vazias de uma lista de strings. 
# Exemplo: dada a lista [“Olá”, “”, “meu”, “nome”, “”, “é”, “facilitador”, “”] a saída deve ser
# [“Olá”, “meu”, “nome”, “é”, “facilitador”]

lista_com_espacos = ["Olá", "", "meu", "nome", "", "é", "facilitador", ""]

for palavra in lista_com_espacos:
    if palavra == "":
        indice = lista_com_espacos.index(palavra)
        lista_com_espacos.pop(indice)

print(lista_com_espacos)