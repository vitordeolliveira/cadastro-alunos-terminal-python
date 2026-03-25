import os
def limpartela():
    os.system('cls' if os.name == 'nt' else 'clear')

def tabela():
    print('-' * 30) 
    print("ESCOLA MUNICIPAL".center(30))
    print('-' * 30) 
    print("\n[1] = ADICIONAR ALUNO\n[2] = LISTAR TODOS OS ALUNOS\n[3] = BUSCAR ALUNO PELO NOME\n[4] = REMOVER ALUNO\n[5] = MOSTRAR MEDIA GERAL DA TURMA\n[6] = SAIR\n")
    try:
        x = int(input('Escolha: '))
    except Exception as erro:
        print(f'ERRO!!! {erro.__class__}')
        print('Por Favor Digite Um Numero Inteiro Valído: ')
        x = int(input('Tente Novamente: '))
    return x


                
