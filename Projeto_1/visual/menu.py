import os
from main import lista_alunos
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
        print(f'ERRO!!! {erro}')
        print('Por Favor Digite Um Numero Inteiro Valído: ')
        x = int(input('Tente Novamente: '))
    return x

def adicionar_aluno():
    nome = input("DIGITE O NOME DO ALUNO: ").strip().upper()
    idade = int(input(f"QUAL É A IDADE DO/A {nome}: "))
    nota = float(input(f"QUAL FOI A NOTA DO/A {nome}: "))
    dicionario_escolar = {
    "Nome Do Aluno":nome,
    "Idade Do Aluno":idade,
    "Nota Do Aluno":nota
}
    lista_alunos.append(dicionario_escolar)

def media_turma():
    limpartela()
    md = 0
    if len(lista_alunos) == 0:
        return "NAO HÁ ALUNOS REGISTRADOS"
    soma = 0
    for aluno in lista_alunos:
        soma += aluno['Nota Do Aluno']
    md = soma / len(lista_alunos)
    return f"A MEDIA DA TURMA É {md:.2f}"

def buscar():
    limpartela()
    busca = input("QUAL ALUNO DESEJA PROCURAR: ").strip().upper()
    for aluno in lista_alunos:
        if aluno["Nome Do Aluno"] == busca:
            return f"Aluno:{busca} ENCONTRADO/A"
    else:
        return f"Aluno:{busca} NAO FOI ENCONTRADO/A"
        
def remover_aluno():
    limpartela()
    remover = input("QUAL ALUNO DESEJA REMOVER: ").strip().upper()
    for aluno in lista_alunos:
        if aluno["Nome Do Aluno"] == remover:
            lista_alunos.remove(aluno)
            return f"Aluno:{remover} REMOVIDO COM SUCESSO"
    else:
        return f"Aluno:{remover} NAO EXISTE"
                
