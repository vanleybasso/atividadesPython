# 5) Monte um sistema com cadastro para: Alunos; Professores; Cursos;

Utilize conjuntos e orientação a objeto.

class Alunos:
    def __init__(self, documento, nome, matricula, curso):
        self.documento = documento
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
    
        

class Curso:
    def __init__(self, nome, periodo):
        self.nome = nome
        self.periodo = periodo

class Professor:
    def __init__(self, nome, disciplina, siape, curso):
        self.nome = nome
        self.disciplina = disciplina
        self.siape = siape
        self.curso = curso
        
#Em outro arquivo

from cadastro import Alunos, Curso, Professor

ads = Curso("Análise e Desenvolvimento de Sistemas", "Matinal")
biologia = Curso("Lic. Ciências Biológicas", "Matinal")
agronomia = Curso("Agronomia", "Integral")

aluno_vanley = Alunos("05455456546", "Vanley", "05456", ads)
aluno_francis = Alunos("565465495", "Francis", "78921", agronomia)
aluno_lucas = Alunos("31358788", "Lucas", "4589", biologia)

profiuri = Professor("Iuri", "Programação", "545", ads)
profmaisa = Professor("Maisa", "Inglês", "789", agronomia)
profluis = Professor("Luis", "Redes", "789", biologia)


print (profmaisa.curso.nome)

 
