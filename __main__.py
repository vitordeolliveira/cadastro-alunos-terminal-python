from visual.menu import *
from visual.funcoes import *
import time

while True:
    limpartela()
    valor = tabela()
    match valor:
        case 1:
           adicionar_aluno()
        case 2:
            limpartela()
            for alunos in lista_alunos:
                print(alunos["Nome Do Aluno"])
            time.sleep(2)

        case 3:
            limpartela()
            print (buscar()) 
            time.sleep(2)     
        case 4:
            limpartela()
            print (remover_aluno())
            time.sleep(2)
        case 5:
            limpartela()
            print (media_turma())
            time.sleep(2)
        case _:
            break