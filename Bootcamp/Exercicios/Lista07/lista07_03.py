'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Sétima Lista de Exercicios - POO
Julho/2022.
'''

# Exercício 3) Crie uma classe ListaPersonalizada que calcule média simples e ponderada.

class ListaPersonalizada(list):
    
    def MediaSimples(self):
        return print(sum(self)/len(self))
    
    def MediaPonderada(self, pesos: list):
        
        numerador = 0
        for indice in range(len(pesos)):
            numerador += (self[indice]*pesos[indice])
        return print(numerador/sum(pesos))
    