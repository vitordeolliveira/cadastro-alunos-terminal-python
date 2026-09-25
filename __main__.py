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
            print("\n" + "="*85)
            print(f"{'ID':<5} | {'NOME DO ALUNO':<30} | {'ANO NASC.':<10} | {'NOTA':<6}")
            print("="*85)
            for aluno in lista_alunos:
                id_aluno = aluno.get("ID", "-")
                nome = aluno.get("Nome Do Aluno", "Não Informado")
                ano = aluno.get("Ano De Nascimento Do Aluno(A)", 0)
                nota = aluno.get("Nota Do Aluno(A)", 0.0)
            print(f"{id_aluno:<5} | "
                f"{nome:<30} | "
                f"{ano:<10} | "
                f"{nota:<6.1f}")
    
            print("="*85 + "\n")
            time.sleep(5)


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