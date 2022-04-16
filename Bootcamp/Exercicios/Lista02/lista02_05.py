'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Segunda Lista de Exercicios - Listas
Março/2022.
'''

#Exercício 5) Dada a lista: lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]. Adicione o elemento 
# 7000 logo após o elemento 6000, o resultado deverá ser: 
# lst = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40].

lst = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
lst[2][2].append(7000)
print(lst)