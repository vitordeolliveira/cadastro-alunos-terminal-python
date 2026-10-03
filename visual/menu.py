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
        print("\n[1] = Adicionar aluno(a)\n[2] = Listar todos os alunos(as)\n[3] = Buscar aluno pelo nome\n[4] = Remover aluno pelo ID\n[5] = Mostrar relatório da turma\n[6] = Sair\n")
        print("=" * 50)
        try:
            x = int(input('ESCOLHA: '))
            if (x <= 0) or (x > 6):
                limpartela()
                print("O número digitado não está entre [1 e 6], TENTE NOVAMENTE! ")
                time.sleep(5)
                continue
            else:
                return x
        except ValueError:
            print("Erro de digitação, por favor digite um número inteiro válido! ")
            time.sleep(5)
            continue


def tabela_relatorio():
    while True:
            limpartela()
            print ("""
                [1] Exibir média geral da turma
                [2] Exibir maior nota da turma
                [3] Exibir menor nota da turma
                [4] Voltar""")
            try:
                valor = int(input())
                if (valor <= 0) or (valor > 4):
                    limpartela()
                    print("O número digitado não está entre [1 e 4], TENTE NOVAMENTE! ")
                    time.sleep(5)
                    continue
                else:
                    return valor
            except ValueError:
                limpartela()
                print("Erro de digitação, por favor digite um número inteiro válido! ")
                time.sleep(5)
                continue


def tabela_atualizacao():
    while True:
        limpartela()
        print ("""
            [1] Atualizar nome/sobrenome do aluno(a)
            [2] Atualizar ano de nascimento do aluno(a)
            [3] Atualizar nota do aluno(a)
            [4] Voltar""")
        try:
            valor = int(input())
            if (valor <= 0) or (valor > 4):
                limpartela()
                print("O número digitado não está entre [1 e 4], TENTE NOVAMENTE! ")
                time.sleep(5)
                continue
            else:
                return valor
        except ValueError:
            limpartela()
            print("Erro de digitação, por favor digite um número inteiro válido! ")
            time.sleep(5)
            continue
