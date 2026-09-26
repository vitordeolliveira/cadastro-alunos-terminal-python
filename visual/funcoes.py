import time
from visual.menu import limpartela
lista_alunos = []
id = 1

def adicionar_aluno():
    global id
    status = ""
    nome = input("DIGITE O NOME/SOBRENOME DO ALUNO: ").strip().upper()
    ano_nsc = int(input(f"QUAL É O ANO DE NASCIMENTO DO ALUNO(A) {nome}: "))
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
    "Nome Do Aluno" : nome,
    "Ano De Nascimento Do Aluno" : ano_nsc,
    "Nota Do Aluno" : nota,
    "Status" : status
}
    lista_alunos.append(tabela)
    id += 1
    limpartela()
    print("Aluno adicionado com sucesso!\n")
    time.sleep(2)

def listar_alunos():
    print("\n" + "="*85)
    print(f"{'ID':<5} | {'NOME DO ALUNO':<30} | {'ANO NASC.':<10} | {'NOTA':<6} | {'STATUS':<8}")
    print("="*85)
    for aluno in lista_alunos:
        id_aluno = aluno.get("ID", "-")
        nome = aluno.get("Nome Do Aluno", "Não Informado")
        ano = aluno.get("Ano De Nascimento Do Aluno", 0)
        nota = aluno.get("Nota Do Aluno", 0.0)
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
        soma += aluno["Nota Do Aluno"]
    md = soma / len(lista_alunos)
    return f"A MEDIA DA TURMA É {md:.2f}"

def excluir_aluno():
    delete = int(input("Qual É O ID Do Aluno(A): "))
    for aluno in lista_alunos:
        if aluno["ID"] == delete:
            resp = input(f"Deseja Realmente Excluir O Aluno(A) {aluno["Nome Do Aluno"]} [S/N]").strip().upper()
            if resp == "S":
                lista_alunos.remove(aluno)
                return f"ALUNO {aluno["Nome Do Aluno"]} PORTADOR DO ID {aluno["ID"]} REMOVIDO COM SUCESSO"
            else:
                return f"OPERAÇÃO CANCELADA"
    else:
        return f"ID NÃO ENCONTRADO"

def buscar_att():
    busca = input("QUAL ALUNO DESEJA PROCURAR: ").strip().upper()
    for aluno in lista_alunos:
        if aluno["Nome Do Aluno"] == busca:
            id_aluno = aluno.get("ID", "-")
            nome = aluno.get("Nome Do Aluno", "Não Informado")
            ano = aluno.get("Ano De Nascimento Do Aluno", 0)
            nota = aluno.get("Nota Do Aluno", 0.0)
            print(f"{'ID':<5} | {'NOME DO ALUNO':<30} | {'ANO NASC.':<10} | {'NOTA':<6}")
            print(f"{id_aluno:<5} | "
                f"{nome:<30} | "
                f"{ano:<10} | "
                f"{nota:<6.1f}")
            atualizar = input("DESEJA ATUALIZAR OS DADOS DO ALUNO(A) S/N").strip().upper()
            if atualizar == "S":
                print ("""
                        [1] ATUALIZAR NOME/SOBRENOME
                        [2] ATUALIZAR ANO DE NASCIMENTO
                        [3] ATUALIAR NOTA DO ALUNO(A)
                        [4] SAIR""")
                valor = int(input())
                match valor:
                    case 1:
                        nome = input("DIGITE O NOME/SOBRENOME DO ALUNO(A): ").strip().upper()
                        aluno["Nome Do Aluno"] = nome
                    case 2:
                        data_ncs = int(input(f"DIGITE O ANO DE NASCIMENTO DO(A) {nome}: "))
                        aluno["Ano De Nascimento Do Aluno"] = data_ncs
                    case 3:
                        nota = float(input(f"QUAL FOI A NOTA DO(A) {nome}: "))
                        if (nota > 10 or nota < 0):
                            print("DIGITE UMA NOTA VALÍDA ENTRE 0-10: ")
                            return
                        else:
                            aluno["Nota Do Aluno"] = nota
                            if (nota <= 5):
                                aluno["Status"] = "REPROVADO(A)"
                            elif (nota <=7):
                                aluno["Status"] = "RECUPERAÇÃO"
                            else:
                                aluno["Status"] = "APROVADO(A)"
                    case _:
                        return
    else:
        return f"ALUNO NÃO CADASTRADO"
