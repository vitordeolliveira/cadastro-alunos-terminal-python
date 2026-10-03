import time
from visual.menu import *
lista_alunos = []
id = 1

def adicionar_aluno():
    global id
    status = ""
    while True:
        nome = input("Digite nome/sobrenome: ").strip().upper()
        if (nome == "") or (not(nome.replace(" ","").isalpha())):
            print("O nome digitado não é válido, por favor digite apenas letras!")
            time.sleep(5)
            limpartela()
            continue
        try:
            ano_nsc = int(input(f"Qual é o ano de nascimento do aluno(a) {nome}: "))
            if not (2000 <= ano_nsc <= 2020):
                limpartela()
                print("Ano fora do intervalo permitido!")
                time.sleep(5)
                continue
            nota = float(input(f"Qual foi a nota do(a) aluno(a) {nome}: "))
            if (nota > 10 or nota < 0):
                limpartela()
                print("A nota digitada não está entre [0 e 10]: ")
                time.sleep(5)
                continue
        except ValueError:
            limpartela()
            print("Erro de digitação, por favor digite apenas números válidos! ")
            time.sleep(5)
            continue
        if (nota <= 5):
            status = "REPROVADO(A)"
        elif (nota <=7):
            status = "RECUPERAÇÃO"
        else:
            status = "APROVADO(A)"
        tabela = {
            'ID' : id,   
            'Nome' : nome,
            'ano_nascimento' : ano_nsc,
            'nota' : nota,
            'Status' : status
        }
        lista_alunos.append(tabela)
        id += 1
        limpartela()
        cont = input ("Deseja adicionar outro aluno(a)?: [S/N]").strip().upper()
        if (cont == "S") or (cont == "SIM"):
            limpartela()
            continue
        else:
            break
 
    limpartela()
    print("Alunos(as) adicionados com sucesso!\n")
    time.sleep(5)

def listar_alunos():
    print("\n" + "="*85)
    print(f"{'ID':<5} | {'NOME DO ALUNO':<30} | {'ANO NASC.':<10} | {'NOTA':<6} | {'STATUS':<8}")
    print("="*85)
    for aluno in lista_alunos:
        id_aluno = aluno.get('ID', "-")
        nome = aluno.get('Nome', "Não Informado")
        ano = aluno.get('ano_nascimento', 0)
        nota = aluno.get('nota', 0.0)
        status = aluno.get('Status' , "-")

        print(f"{id_aluno:<5} | "
            f"{nome:<30} | "
            f"{ano:<10} | "
            f"{nota:<6.1f} |"
            f"{status:<8}")
        
    print("="*85 + "\n")

def relatorio():
    while True:
        valor = tabela_relatorio()
        match valor:
            case 1:
                if len(lista_alunos) == 0:
                    return "Não há alunos(as) cadastrados!"
                else:
                    soma = 0
                    for aluno in lista_alunos:
                        soma += aluno['nota']
                    md = soma / len(lista_alunos)
                    return f"A média da turma é {md:.2f}"
            case 2:
                if len(lista_alunos) == 0:
                    return "Não há alunos(as) cadastrados!"
                else:
                    maior_nt = lista_alunos[0]['nota']
                    nome = lista_alunos[0]['Nome']
                    for aluno in lista_alunos:
                        nt_atual = aluno['nota']
                        if maior_nt < nt_atual:
                            maior_nt = nt_atual
                            nome = aluno['Nome']
                    return f"A maior nota é do(a) aluno(a) {nome} com nota {maior_nt:.2f} "
            case 3:
                if len(lista_alunos) == 0:
                    return "Não há alunos(as) cadastrados"
                else:
                    menor_nt = lista_alunos[0]['nota']
                    nome = lista_alunos[0]['Nome']
                    for aluno in lista_alunos:
                        nt_atual = aluno['nota']
                        if menor_nt > nt_atual:
                            menor_nt = nt_atual
                            nome = aluno['Nome']
                    return f"A menor nota é do aluno(a) {nome} com nota {menor_nt:.2f} "
            case 4:
                return "Operação cancelada!"
            

def excluir_aluno():
    try:
        delete = int(input("Qual é o ID do aluno(a): "))
    except ValueError:
        limpartela()
        return("Erro de digitação, por favor digite um número inteiro válido!")
    for aluno in lista_alunos:
        if aluno['ID'] == delete:
            resp = input(f"Deseja realmente excluir o aluno(A) {aluno['Nome']} [S/N]").strip().upper()
            if resp == "S" or resp == "SIM":
                lista_alunos.remove(aluno)
                return f"Aluno {aluno['Nome']} portador do ID {aluno['ID']} removido com sucesso!"
            else:
                return "Operação cancelada!"
    return "ID não cadastrado"

def buscar():
    busca = input("Qual é o nome do aluno(a): ").strip().upper()
    if (busca == "") or (not(busca.replace(" ","").isalpha())):
        return("O nome digitado não é válido, por favor digite apenas letras!")
    for aluno in lista_alunos:
        if aluno['Nome'] == busca:
            id_aluno = aluno.get('ID', "-")
            nome = aluno.get('Nome', "Não Informado")
            ano = aluno.get('ano_nascimento', 0)
            nota = aluno.get('nota', 0.0)
            print(f"{'ID':<5} | {'NOME DO ALUNO':<30} | {'ANO NASC.':<10} | {'NOTA':<6}")
            print(f"{id_aluno:<5} | "
                f"{nome:<30} | "
                f"{ano:<10} | "
                f"{nota:<6.1f}")
            atualizar = input(f"Deseja atualizar os dados do aluno(a) {busca}? S/N: ").strip().upper()
            if (atualizar == "S" or atualizar == "SIM"):
                return(atualizar_aluno(aluno))   
            else:
                return("Operação cancelada!")            
    else:
        return (f"Não há aluno(a) {busca} cadastrado!")

def atualizar_aluno(aluno:dict):
    while True:
        valor = tabela_atualizacao()
        match valor:
            case 1:
                nome = input("Digite o nome/sobrenome do aluno(a): ").strip().upper()
                if (nome == "") or (not(nome.replace(" ","").isalpha())):
                    print("O nome digitado não é válido, por favor digite apenas letras!")
                    time.sleep(5)
                    limpartela()
                    continue
                else:
                    aluno["Nome"] = nome
                    print("Alterações feitas com sucesso!")
                    cont = input ("Deseja alterar outro dado do(a) aluno(a)?: [S/N]").strip().upper()
                    if (cont == "S") or (cont == "SIM"):
                        limpartela()
                        continue
                    else:
                        return("Operação cancelada!")
                        
            case 2:
                try:
                    data_ncs = int(input(f"Digite o ano de nascimento do aluno(a) {aluno['Nome']}: "))
                    if not (2000 <= data_ncs <= 2020):
                        print("Ano fora do intervalo permitido! ")
                        time.sleep(5)
                        continue
                except ValueError:
                    print("Erro de digitação, por favor digite um número inteiro válido!")
                    time.sleep(5)
                    continue
                else:
                    aluno['ano_nascimento'] = data_ncs
                    print("Alterações feitas com sucesso!")
                    cont = input ("Deseja alterar outro dado do(a) aluno(a)?: [S/N]").strip().upper()
                    if (cont == "S") or (cont == "SIM"):
                        limpartela()
                        continue
                    else:
                        return("Operação cancelada!")
                        
            case 3:
                try:
                    nota = float(input(f"Qual foi a nota do aluno(a) {aluno['Nome']}: "))
                except ValueError:
                    print("Erro de digitação, por favor digite um número entre [0 e 10]! ")
                    time.sleep(5)
                    continue
                if (nota > 10 or nota < 0):
                    print("Digite uma nota entre [0 e 10]: ")
                    time.sleep(5)
                    continue
                else:
                    aluno["nota"] = nota
                    if (nota <= 5):
                        aluno["Status"] = "REPROVADO(A)"
                    elif (nota <=7):
                        aluno["Status"] = "RECUPERAÇÃO"
                    else:
                        aluno["Status"] = "APROVADO(A)"
                print("Alterações feitas com sucesso!")
                cont = input ("Deseja alterar outro dado do(a) aluno(a)?: [S/N]").strip().upper()
                if (cont == "S") or (cont == "SIM"):
                    limpartela()
                    continue
                else:
                    return("Operação cancelada!")
            case 4:
                return("Operação cancelada!")
    
