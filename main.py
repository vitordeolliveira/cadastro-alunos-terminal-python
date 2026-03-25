from visual import menu
import time

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
    menu.limpartela()
    md = 0
    if len(lista_alunos) == 0:
        return "NAO HÁ ALUNOS REGISTRADOS"
    soma = 0
    for aluno in lista_alunos:
        soma += aluno['Nota Do Aluno']
    md = soma / len(lista_alunos)
    return f"A MEDIA DA TURMA É {md:.2f}"

def remover_aluno():
    menu.limpartela()
    remover = input("QUAL ALUNO DESEJA REMOVER: ").strip().upper()
    for aluno in lista_alunos:
        if aluno["Nome Do Aluno"] == remover:
            lista_alunos.remove(aluno)
            return f"Aluno:{remover} REMOVIDO COM SUCESSO"
    else:
        return f"Aluno:{remover} NAO EXISTE"

def buscar():
    menu.limpartela()
    busca = input("QUAL ALUNO DESEJA PROCURAR: ").strip().upper()
    for aluno in lista_alunos:
        if aluno["Nome Do Aluno"] == busca:
            return f"Aluno:{busca} ENCONTRADO/A"
    else:
        return f"Aluno:{busca} NAO FOI ENCONTRADO/A"
        


lista_alunos = []
while True:
    menu.limpartela()
    valor = menu.tabela()
    match valor:
        case 1:
           adicionar_aluno()
        case 2:
            menu.limpartela()
            for alunos in lista_alunos:
                print(alunos["Nome Do Aluno"])
            time.sleep(2)

        case 3:
            print (buscar()) 
            time.sleep(2)     
        case 4:
            print (remover_aluno())
            time.sleep(2)
        case 5:
            print (media_turma())
            time.sleep(2)
        case _:
            break