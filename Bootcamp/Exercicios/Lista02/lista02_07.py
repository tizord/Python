'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Segunda Lista de Exercicios - Listas
Março/2022.
'''

#Exercício 7) Dada a lista de strings ["1", "7", "99", "15"] construa um programa que converte 
# todos os elementos desta lista para inteiro

lista_str = ["1", "7", "99", "15"]

lista_int = list(map(int, lista_str))

print(f"{'-'*35}\n CONVERTE STR EM INT:\n{'-'*35}")

for elemento in lista_int:
    indice = lista_int.index(elemento)
    classe = type(lista_int[indice])
    print(f"O elemento {elemento} é do tipo {classe}")

lista2_str = list(map(str, lista_int))

print(f"{'-'*35}\n CONVERTE INT EM STR:\n{'-'*35}")

for elemento in lista2_str:
    indice = lista2_str.index(elemento)
    classe = type(lista2_str[indice])
    print(f"O elemento {elemento} é do tipo {classe}")