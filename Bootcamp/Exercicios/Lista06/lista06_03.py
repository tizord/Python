'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Sexta Lista de Exercicios - Funções
Abril/2022.
'''

#Exercício 3) Faça uma função que retorne o reverso de um número inteiro informado. 
# Por exemplo: 127 -> 721.

def Devolve_Reverso(numero: int) -> int:
    '''
    Essa função devolve o reverso de um número.

        Arg:
        numero: int

        Output:
        numero_reverso: int
    
    '''
    numero_str = str(numero)
    numero_reverso = int("".join(reversed(numero_str)))

    return numero_reverso

print(f'O reverso do número 127 é {Devolve_Reverso(127)}')
print(f'O reverso do número 99827 é {Devolve_Reverso(99827)}')