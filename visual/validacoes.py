import os
import time
from datetime import date

def limpartela():
    os.system('cls' if os.name == 'nt' else 'clear')


def tabela():
    while True:
        limpartela()
        print('=' * 50) 
        print("ESCOLA MUNICIPAL".center(30))
        print('=' * 50) 
        print("""[1] = Adicionar aluno(a)
[2] = Listar todos os alunos
[3] = Buscar aluno pelo nome
[4] = Remover aluno pelo ID
[5] = Mostrar relatório da turma
[6] = Sair""")
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
            print('=' * 40) 
            print("RELATÓRIO DA TURMA".center(30))
            print('=' * 40) 
            print ("""[1] Exibir média geral da turma
[2] Exibir maior nota da turma
[3] Exibir menor nota da turma
[4] Voltar""")
            print("=" * 40)
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
        print('=' * 40) 
        print("ATUALIZAR ALUNO(A)".center(30))
        print('=' * 40) 
        print ("""[1] Atualizar nome/sobrenome do aluno(a)
[2] Atualizar ano de nascimento do aluno(a)
[3] Atualizar nota do aluno(a)
[4] Voltar""")
        print('=' * 40)
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

def validar_nome(nome):
    if (nome == "") or (not(nome.replace(" ","").isalpha())) or (len(nome) < 3):
        print("O nome digitado não é válido, por favor digite apenas letras!")
        time.sleep(5)
        limpartela()
        return False
    else:
        return True

def validar_ano(ano):
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade > 18 or idade < 3:
        print ("Aluno(a) com idade superior a 18 ou menor do que 3!")
        time.sleep(5)
        limpartela()
        return False
    else:
        return True
    
def validar_nota(nota):
    if (nota > 10 or nota < 0):
        limpartela()
        print("A nota digitada não está entre [0 e 10]: ")
        time.sleep(5)
        return False
    else:
        return True
