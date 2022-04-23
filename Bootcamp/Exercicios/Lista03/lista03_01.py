'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Terceira Lista de Exercicios - Sets
Abril/2022.
'''

#Exercício 1)

alunos_ingles ={
    "João Alves dos Santos",
    "Maria Magalhães",
    "Antônio da Silva Ferreira",
    "José Júnior Jarbas",
    "Henrique da Silva Sauro",
    "Joaquina Ferreira da Silva",
    "Fabiana Aparecida Bianco",
    "Marrone Gutierres",
    "Carlos Magno Farad",
    "Antônio da Silva Júnior Amaral"}

alunos_frances = {
    "João Alves dos Santos",
    "Antônio da Silva Ferreira",
    "Fernanda Abdala Mohamed",
    "Abner Mignon Alib",
    "Alisson Figueiredo",
    "Henrique da Silva Sauro",
    "Maria Magalhães",
    "Marrone Gutierres",
    "Joaquina Ferreira da Silva"}

total_alunos = alunos_ingles | alunos_frances
print(f"\nA escola possui {len(total_alunos)} alunos\n")

alunos_exclusivos_ingles = alunos_ingles - alunos_frances
print(f"A escola possui {len(alunos_exclusivos_ingles)} alunos matriculados APENAS em INGLES, e os alunos são:\n\n {alunos_exclusivos_ingles}\n")

alunos_exclusivos_frances = alunos_frances - alunos_ingles
print(f"A escola possui {len(alunos_exclusivos_frances)} alunos matriculados APENAS em FRANCES, e os alunos são:\n\n {alunos_exclusivos_frances}\n")

alunos_ambos_cursos = alunos_ingles & alunos_frances
print(f"A escola possui {len(alunos_ambos_cursos)} alunos matriculados em AMBOS OS CURSOS, e os alunos são:\n\n {alunos_ambos_cursos}\n")

alunos_ou_frances_ou_ingles = alunos_ingles ^ alunos_frances
print(f"\nA escola possui {len(alunos_ou_frances_ou_ingles)} matriculados OU em Inglês OU em francês\n")