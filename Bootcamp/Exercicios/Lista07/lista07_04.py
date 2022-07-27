'''
/Codigo[S] - Stone e Howbootcamps
Aluno: Thiago William

Sétima Lista de Exercicios - POO
Julho/2022.
'''

# Exercício 4) Utilizando Herança e Polimorfismo reduza a quantidade de if-elses.

# class Passaro: 
#     def calcula_velocidade(self):

#         if self.tipo == “EUROPEU”:
#             return self.calcula_velocidade_base()

#         elif self.tipo == “AFRICANO”:
#             return self.calcula_velocidade_base() - self.calcula_fator_carga() * self.altura_maxima_de_voo()

#         elif self.tipo == “NORUEGUES”:
#             return 0 if self.nao_voa else calcula_velocidade_base()


class Passaro:

    def calcula_velocidade_base(self):
        pass
class Europeu(Passaro):
    def calcula_velocidade(self):
        return self.calcula_velocidade_base()

class AFRICANO(Passaro):
    def calcula_fator_carga():
        return calcula_fator_carga
    
    def altura_maxima_de_voo():
        return altura_maxima_de_voo

    def calcula_velocidade(self):        
        self.calcula_velocidade_base() - self.calcula_fator_carga() * self.altura_maxima_de_voo()

class NORUEGUES(Passaro):
    def nao_voa(self):
        return 0
    def calcula_velocidade(self):
        return calcula_velocidade_base()