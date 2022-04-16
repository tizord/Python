'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Segunda Lista de Exercicios - Listas
Março/2022.
'''

#Exercício 3) Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas respectivas
#posições

lista3 = [1, 3, 5, 7, 9, 11]

maior = max(lista3)
menor = min(lista3)

indice_maior = lista3.index(maior)
indice_menor = lista3.index(menor)

print(f"O elemento de maior valor é {maior} e está na posição {indice_maior}")
print(f"O elemento de menor valor é {menor} e está na posição {indice_menor}")

