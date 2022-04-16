'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Segunda Lista de Exercicios - Listas
Março/2022.
'''

#Exercício 1) Crie uma variável do tipo lista com 5 elementos. Imprima na tela
# o elemento e sua posição na lista

lista = [1, 'segundo', [3,3,3], 4.0, 'cinco']

for i in lista:
    print(f'Elemento {i} na posição {lista.index(i)}')
