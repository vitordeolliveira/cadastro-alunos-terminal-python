import os
def limpartela():
    os.system('cls' if os.name == 'nt' else 'clear')

def tabela():
    print('=' * 50) 
    print("ESCOLA MUNICIPAL".center(30))
    print('=' * 50) 
    print("\n[1] = ADICIONAR ALUNO's(A)\n[2] = LISTAR TODOS OS ALUNOS\n[3] = BUSCAR ALUNO PELO NOME\n[4] = REMOVER ALUNO PELO ID\n[5] = MOSTRAR MEDIA GERAL DA TURMA\n[6] = SAIR\n")
    print("=" * 50)
    while True:
        try:
            x = int(input('ESCOLHA: '))
        except ValueError:
            print(f'ERRO!!!')
            print('POR FAVOR DIGITE UM NÚMERO INTEIRO VALÍDO: ')
            continue
        break
    return x

                
