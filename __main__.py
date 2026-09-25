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
            listar_alunos()
            time.sleep(5)
        case 3:
            limpartela()
            buscar_att() 
            time.sleep(5)     
        case 4:
            limpartela()
            print (excluir_aluno())
            time.sleep(5)
        case 5:
            limpartela()
            print (media_turma())
            time.sleep(5)
        case _:
            break