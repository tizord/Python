'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Quinta Lista de Exercicios - laço de repetição
Abril/2022.
'''

# Exercício 5) Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
# A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. 
# Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo 
# atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada 
# (retirar o melhor e o pior salto e depois calcular a média com as notas restantes).

print('Insira o nome e as notas do atleta')

atleta = input("Atleta: ")

notas = []

for _ in range (7):
    nota = float(input('Nota: '))
    notas.append(nota)

melhor_nota = max(notas)
pior_nota = min(notas)

notas.remove(melhor_nota)
notas.remove(pior_nota)

media = sum(notas)/len(notas)



print('\n\nResultado final:')
print(f'Atleta: {atleta}')
print(f'Melhor nota: {melhor_nota}')
print(f'Pior nota: {pior_nota}')
print(f'Média: {media:.2f}')