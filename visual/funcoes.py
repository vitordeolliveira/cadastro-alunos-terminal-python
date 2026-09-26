import time
from visual.menu import limpartela
lista_alunos = []
id = 1

def adicionar_aluno():
    global id
    status = ""
    nome = input("DIGITE O NOME/SOBRENOME: ").strip().upper()
    ano_nsc = int(input(f"QUAL É O ANO DE NASCIMENTO DO(A) {nome}: "))
    nota = float(input(f"QUAL FOI A NOTA DO(A) {nome}: "))
    if (nota > 10 or nota < 0):
        print("DIGITE UMA NOTA VALÍDA ENTRE 0-10: ")
        return
    else:
        if (nota <= 5):
            status = "REPROVADO(A)"
        elif (nota <=7):
            status = "RECUPERAÇÃO"
        else:
            status = "APROVADO(A)"

    tabela = {
    "ID" : id,   
    "Nome" : nome,
    "ano_nascimento" : ano_nsc,
    "nota" : nota,
    "Status" : status
}
    lista_alunos.append(tabela)
    id += 1
    limpartela()
    print("ALUNO ADICIONADO COM SUCESSO!\n")
    time.sleep(2)

def listar_alunos():
    print("\n" + "="*85)
    print(f"{'ID':<5} | {'NOME DO ALUNO':<30} | {'ANO NASC.':<10} | {'NOTA':<6} | {'STATUS':<8}")
    print("="*85)
    for aluno in lista_alunos:
        id_aluno = aluno.get("ID", "-")
        nome = aluno.get("Nome", "Não Informado")
        ano = aluno.get("ano_nascimento", 0)
        nota = aluno.get("nota", 0.0)
        status = aluno.get("Status" , "-")

        print(f"{id_aluno:<5} | "
            f"{nome:<30} | "
            f"{ano:<10} | "
            f"{nota:<6.1f} |"
            f"{status:<8}")
        
    print("="*85 + "\n")

def media_turma():
    if len(lista_alunos) == 0:
        return "NAO HÁ ALUNOS REGISTRADOS"
    soma = 0
    for aluno in lista_alunos:
        soma += aluno["nota"]
    md = soma / len(lista_alunos)
    return f"A MEDIA DA TURMA É {md:.2f}"

def excluir_aluno():
    delete = int(input("Qual É O ID Do Aluno(A): "))
    for aluno in lista_alunos:
        if aluno["ID"] == delete:
            resp = input(f"Deseja Realmente Excluir O Aluno(A) {aluno["Nome"]} [S/N]").strip().upper()
            if resp == "S":
                lista_alunos.remove(aluno)
                return f"ALUNO {aluno["Nome"]} PORTADOR DO ID {aluno["ID"]} REMOVIDO COM SUCESSO"
            else:
                return f"OPERAÇÃO CANCELADA"
    else:
        return f"ID NÃO ENCONTRADO"

def buscar():
    busca = input("QUAL ALUNO DESEJA PROCURAR: ").strip().upper()
    for aluno in lista_alunos:
        if aluno["Nome"] == busca:
            id_aluno = aluno.get("ID", "-")
            nome = aluno.get("Nome", "Não Informado")
            ano = aluno.get("ano_nascimento", 0)
            nota = aluno.get("nota", 0.0)
            print(f"{'ID':<5} | {'NOME DO ALUNO':<30} | {'ANO NASC.':<10} | {'NOTA':<6}")
            print(f"{id_aluno:<5} | "
                f"{nome:<30} | "
                f"{ano:<10} | "
                f"{nota:<6.1f}")
            atualizar = input("DESEJA ATUALIZAR OS DADOS DO ALUNO(A) S/N: ").strip().upper()
            if atualizar == "S":
                atualizar_aluno(aluno)
                return
            else:
                print("OPRAÇÃO CANCELADA")
                return
    else:
        print ("ALUNO NÃO CADASTRADO")

def atualizar_aluno(aluno:dict):
        print ("""
                [1] ATUALIZAR NOME/SOBRENOME
                [2] ATUALIZAR ANO DE NASCIMENTO
                [3] ATUALIAR NOTA DO ALUNO(A)
                [4] SAIR""")
        valor = int(input())
        match valor:
            case 1:
                nome = input("DIGITE O NOME/SOBRENOME(A): ").strip().upper()
                aluno["Nome"] = nome
                print("ALTERAÇÕES FEITAS COM SUCESSO!")
                time.sleep(2)
            case 2:
                data_ncs = int(input(f"DIGITE O ANO DE NASCIMENTO DO(A) {aluno["Nome"]}: "))
                aluno["ano_nascimento"] = data_ncs
                print("ALTERAÇÕES FEITAS COM SUCESSO!")
                time.sleep(2)
            case 3:
                nota = float(input(f"QUAL FOI A NOTA DO(A) {aluno["Nome"]}: "))
                if (nota > 10 or nota < 0):
                    print("DIGITE UMA NOTA VALÍDA ENTRE 0-10: ")
                    return
                else:
                    aluno["nota"] = nota
                    if (nota <= 5):
                        aluno["Status"] = "REPROVADO(A)"
                    elif (nota <=7):
                        aluno["Status"] = "RECUPERAÇÃO"
                    else:
                        aluno["Status"] = "APROVADO(A)"
                print("ALTERAÇÕES FEITAS COM SUCESSO!")
                time.sleep(2)
            case _:
                return
    
