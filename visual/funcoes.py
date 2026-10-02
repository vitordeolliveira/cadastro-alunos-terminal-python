import time
from visual.menu import *
lista_alunos = []
id = 1

def adicionar_aluno():
    global id
    status = ""
    while True:
        nome = input("DIGITE O NOME/SOBRENOME: ").strip().upper()
        if (nome == "") or (not(nome.replace(" ","").isalpha())):
            print("O NOME DIGITADO NÃO É VALIDO, POR FAVOR DIGITE SOMENTE LETRAS")
            time.sleep(5)
            limpartela()
            continue
        try:
            ano_nsc = int(input(f"QUAL É O ANO DE NASCIMENTO DO(A) {nome}: "))
            if not (2000 <= ano_nsc <= 2020):
                limpartela()
                print("ANO FORA DO INTERVALO PERMITIDO!")
                time.sleep(5)
                continue
            nota = float(input(f"QUAL FOI A NOTA DO(A) {nome}: "))
            if (nota > 10 or nota < 0):
                limpartela()
                print("DIGITE UMA NOTA VALÍDA ENTRE 0/10: ")
                time.sleep(5)
                continue
        except ValueError:
            limpartela()
            print("ERRO DE DIGITAÇÃO POR FAVOR DIGITE APENAS NÚMEROS INTEIROS VALÍDOS! ")
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
        cont = input ("DESEJA ADICIONAR OUTRO ALUNO?: [S/N]").strip().upper()
        if (cont == "S") or (cont == "SIM"):
            limpartela()
            continue
        else:
            break
 
    limpartela()
    print("ALUNO's(A) ADICIONADO COM SUCESSO!\n")
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
                    return "NAO HÁ ALUNOS REGISTRADOS"
                else:
                    soma = 0
                    for aluno in lista_alunos:
                        soma += aluno['nota']
                    md = soma / len(lista_alunos)
                    return f"A MEDIA DA TURMA É {md:.2f}"
            case 2:
                if len(lista_alunos) == 0:
                    return "NAO HÁ ALUNOS REGISTRADOS"
                else:
                    maior_nt = lista_alunos[0]['nota']
                    nome = lista_alunos[0]['Nome']
                    for aluno in lista_alunos:
                        nt_atual = aluno['nota']
                        if maior_nt < nt_atual:
                            maior_nt = nt_atual
                            nome = aluno['Nome']
                    return f"A MAIOR NOTA DA TURMA É DO ALUNO(A) {nome} COM NOTA = {maior_nt:.2F} "
            case 3:
                if len(lista_alunos) == 0:
                    return "NAO HÁ ALUNOS REGISTRADOS"
                else:
                    menor_nt = lista_alunos[0]['nota']
                    nome = lista_alunos[0]['Nome']
                    for aluno in lista_alunos:
                        nt_atual = aluno['nota']
                        if menor_nt > nt_atual:
                            menor_nt = nt_atual
                            nome = aluno['Nome']
                    return f"A MENOR NOTA DA TURMA É DO ALUNO(A) {nome} COM NOTA = {menor_nt:.2F} "
            case 4:
                return "OPERAÇÃO CANCELADA"
            

def excluir_aluno():
    try:
        delete = int(input("QUAL É O ID DO ALINO(A): "))
    except ValueError:
        limpartela()
        return("ERRO DE DIGITAÇÃO, POR FAVOR DIGITE UM NÚMERO INTEIRO VALÍDO!")
    for aluno in lista_alunos:
        if aluno['ID'] == delete:
            resp = input(f"Deseja Realmente Excluir O Aluno(A) {aluno['Nome']} [S/N]").strip().upper()
            if resp == "S" or resp == "SIM":
                lista_alunos.remove(aluno)
                return f"ALUNO {aluno['Nome']} PORTADOR DO ID {aluno['ID']} REMOVIDO COM SUCESSO"
            else:
                return "OPERAÇÃO CANCELADA"
    return "ID NÃO ENCONTRADO"

def buscar():
    busca = input("QUAL ALUNO DESEJA PROCURAR: ").strip().upper()
    if (busca == "") or (not(busca.replace(" ","").isalpha())):
        return("O NOME DIGITADO NÃO É VALIDO, POR FAVOR DIGITE SOMENTE LETRAS")
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
            atualizar = input("DESEJA ATUALIZAR OS DADOS DO ALUNO(A) S/N: ").strip().upper()
            if (atualizar == "S" or atualizar == "SIM"):
                return(atualizar_aluno(aluno))   
            else:
                return("OPERAÇÃO CANCELADA")            
    else:
        return ("ALUNO NÃO CADASTRADO")

def atualizar_aluno(aluno:dict):
    while True:
        valor = tabela_atualizacao()
        match valor:
            case 1:
                nome = input("DIGITE O NOME/SOBRENOME(A): ").strip().upper()
                if (nome == "") or (not(nome.replace(" ","").isalpha())):
                    print("O NOME DIGITADO NÃO É VALIDO, POR FAVOR DIGITE SOMENTE LETRAS")
                    time.sleep(5)
                    limpartela()
                    continue
                else:
                    aluno["Nome"] = nome
                    print("ALTERAÇÕES FEITAS COM SUCESSO!")
                    cont = input ("DESEJA ALTERAR OURTO DADO DO(A) ALUNO?: [S/N]").strip().upper()
                    if (cont == "S") or (cont == "SIM"):
                        limpartela()
                        continue
                    else:
                        return("OPERAÇÃO CANCELADA!")
                        
            case 2:
                try:
                    data_ncs = int(input(f"DIGITE O ANO DE NASCIMENTO DO(A) {aluno['Nome']}: "))
                    if not (2000 <= data_ncs <= 2020):
                        print("ANO FORA DO INTERVALO PERMITIDO! ")
                        time.sleep(5)
                        continue
                except ValueError:
                    print("ERRO DE DIGITAÇÃO, POR FAVOR DIGITE UM NÚMERO VALÍDO!")
                    time.sleep(5)
                    continue
                else:
                    aluno['ano_nascimento'] = data_ncs
                    print("ALTERAÇÕES FEITAS COM SUCESSO!")
                    cont = input ("DESEJA ALTERAR OUTRO DADO DO(A) ALUNO?: [S/N]").strip().upper()
                    if (cont == "S") or (cont == "SIM"):
                        limpartela()
                        continue
                    else:
                        return("OPERAÇÃO CANCELADA!")
                        
            case 3:
                try:
                    nota = float(input(f"QUAL FOI A NOTA DO(A) {aluno['Nome']}: "))
                except ValueError:
                    print("ERRO DE DIGITAÇÃO, POR FAVOR DIGITE UM NÚMERO VALÍDO ENTRE 0/10! ")
                    time.sleep(5)
                    continue
                if (nota > 10 or nota < 0):
                    print("DIGITE UMA NOTA VALÍDA ENTRE 0/10: ")
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
                print("ALTERAÇÕES FEITAS COM SUCESSO!")
                cont = input ("DESEJA ALTERAR OUTRO DADO DO(A) ALUNO?: [S/N]").strip().upper()
                if (cont == "S") or (cont == "SIM"):
                    limpartela()
                    continue
                else:
                    return("OPERAÇÃO CANCELADA!")
            case 4:
                return("OPERAÇÃO CANCELADA!")
    
