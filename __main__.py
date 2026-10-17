from visual.menu import *
from alunos import *
import time
from database import *

if __name__ == "__main__":
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
                print(buscar())
                time.sleep(5)     
            case 4:
                limpartela()
                print (excluir_aluno())
                time.sleep(5)
            case 5:
                limpartela()
                print (relatorio())
                time.sleep(5)
            case 6:
                break