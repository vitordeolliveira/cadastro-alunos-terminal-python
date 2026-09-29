import os
def limpartela():
    os.system('cls' if os.name == 'nt' else 'clear')
import time

def tabela():
    while True:
        limpartela()
        print('=' * 50) 
        print("ESCOLA MUNICIPAL".center(30))
        print('=' * 50) 
        print("\n[1] = ADICIONAR ALUNO's(A)\n[2] = LISTAR TODOS OS ALUNOS\n[3] = BUSCAR ALUNO PELO NOME\n[4] = REMOVER ALUNO PELO ID\n[5] = MOSTRAR MEDIA GERAL DA TURMA\n[6] = SAIR\n")
        print("=" * 50)
        try:
            x = int(input('ESCOLHA: '))
            if (x <= 0) or (x > 6):
                limpartela()
                print("O NÚMERO DIGITADO NÃO ESTÁ ENTRE [1/6], TENTE NOVAMENTE! ")
                time.sleep(5)
                continue
            else:
                return x
        except ValueError:
            print("ERRO DE DIGITAÇÃO, POR FAVOR DIGITE UM NÚMERO INTEIRO VALÍDO! ")
            time.sleep(5)
            continue
        
    
def tabela_atualizacao():
    while True:
        limpartela()
        print ("""
            [1] ATUALIZAR NOME/SOBRENOME
            [2] ATUALIZAR ANO DE NASCIMENTO
            [3] ATUALIAR NOTA DO ALUNO(A)
            [4] VOLTAR""")
        try:
            valor = int(input())
            if (valor <= 0) or (valor > 4):
                limpartela()
                print("O NÚMERO DIGITADO NÃO ESTÁ ENTRE [1/4], TENTE NOVAMENTE! ")
                time.sleep(5)
                continue
            else:
                return valor
        except ValueError:
            limpartela()
            print("ERRO DE DIGITAÇÃO, POR FAVOR DIGITE UM NÚMERO INTEIRO VALÍDO! ")
            time.sleep(5)
            continue
