import time

from database import *
from visual.validacoes import *


def adicionar_aluno():
    while True:
        try:
            nome = input("Digite nome/sobrenome: ").strip().lower()
            resultado = validar_nome(nome)
            if resultado is not True:
                continue
            ano_nsc = int(input(f"Qual é o ano de nascimento do(a) {nome}: "))
            resultado = validar_ano(ano_nsc)
            if resultado is not True:
                continue
            nota = float(input(f"Qual foi a nota do(a) {nome}: "))
            resultado = validar_nota(nota)
            if resultado is not True:
                continue
            insert(nome, ano_nsc, nota)
        except ValueError:
            limpartela()
            print(
                "Erro de digitação, por favor digite apenas números válidos! "
            )
            time.sleep(5)
            continue
        limpartela()
        cont = input("Deseja adicionar outro aluno(a)?: [S/N]").strip().lower()
        if (cont == "s") or (cont == "sim"):
            limpartela()
            continue
        else:
            break
    print("Alunos(as) adicionados com sucesso!\n")
    time.sleep(5)
    limpartela()


def listar_alunos():
    print("\n" + "=" * 85)
    print(
        f"{'ID':<5} | {'NOME DO ALUNO':<30} | {'ANO NASC.':<10} | {'NOTA':<6} |"
    )
    print("=" * 85)
    select_all()
    print("=" * 85 + "\n")


def relatorio():
    while True:
        valor = tabela_relatorio()
        match valor:
            case 1:
                media = avg()
                print("\n" + "=" * 85)
                print(f"A média geral da turma é {media:.2f}")
                print("=" * 85 + "\n")
                time.sleep(5)
            case 2:
                print("\n" + "=" * 85)
                print(
                    f"{'ID':<5} | {'NOME DO ALUNO':<30} | {'ANO NASC.':<10} | {'NOTA':<6} |"
                )
                print("=" * 85)
                buscar_maior_nota()
                print("=" * 85 + "\n")
                time.sleep(5)
            case 3:
                print("\n" + "=" * 85)
                print(
                    f"{'ID':<5} | {'NOME DO ALUNO':<30} | {'ANO NASC.':<10} | {'NOTA':<6} |"
                )
                print("=" * 85)
                buscar_menor_nota()
                print("=" * 85 + "\n")
                time.sleep(5)
            case 4:
                return "Operação cancelada!"


def excluir_aluno():
    try:
        id_aluno = int(input("Qual é o ID do aluno(a) que deseja deletar: "))
    except ValueError:
        limpartela()
        return "Erro de digitação, por favor digite um número inteiro válido!"
    resp = (
        input(
            "Deseja realmente excluir o aluno(a) [S/N]? Confira os dados corretamente, deletar o aluno pode ser irreversível: "
        )
        .strip()
        .lower()
    )
    if resp == "s" or resp == "sim":
        return delete(id_aluno)
    else:
        return "Operação cancelada!"


def buscar():
    buscar = input("Qual é o nome do aluno(a): ").strip().lower()
    resultado = validar_nome(buscar)
    if resultado is not True:
        return "Erro na operação!"
    print(
        f"{'ID':<5} | {'NOME DO ALUNO':<30} | {'ANO NASC.':<10} | {'NOTA':<6}"
    )
    resultado = select_like(buscar)
    if resultado is not True:
        return f"Nenhum aluno(a) {buscar} encontrado! "
    atualizar = (
        input("Deseja atualizar os dados de algun dos alunos(a)? S/N: ")
        .strip()
        .lower()
    )
    if atualizar == "s" or atualizar == "sim":
        try:
            id_aluno = int(input("Qual é o ID do aluno(a): "))
            return atualizar_aluno(id_aluno)
        except ValueError:
            limpartela()
            return (
                "Erro de digitação, por favor digite um número inteiro válido!"
            )
    else:
        return "Operação cancelada!"


def atualizar_aluno(id: int):
    while True:
        valor = tabela_atualizacao()
        match valor:
            case 1:
                nome = (
                    input("Digite o nome/sobrenome do aluno(a): ")
                    .strip()
                    .lower()
                )
                resultado = validar_nome(nome)
                if resultado is not True:
                    continue
                else:
                    print(update_nome(id, nome))
                    cont = (
                        input(
                            "Deseja alterar outro dado do(a) aluno(a)?: [S/N]"
                        )
                        .strip()
                        .lower()
                    )
                    if (cont == "s") or (cont == "sim"):
                        limpartela()
                        continue
                    else:
                        return "Operação cancelada!"

            case 2:
                try:
                    data_ncs = int(
                        input("Digite o ano de nascimento do aluno(a): ")
                    )
                    resultado = validar_ano(data_ncs)
                    if resultado is not True:
                        continue
                except ValueError:
                    print(
                        "Erro de digitação, por favor digite um número inteiro válido!"
                    )
                    time.sleep(5)
                    continue
                else:
                    print(update_ano(id, data_ncs))
                    cont = (
                        input(
                            "Deseja alterar outro dado do(a) aluno(a)?: [S/N]"
                        )
                        .strip()
                        .lower()
                    )
                    if (cont == "s") or (cont == "sim"):
                        limpartela()
                        continue
                    else:
                        return "Operação cancelada!"

            case 3:
                try:
                    nota = float(input("Qual foi a nova nota do aluno(a): "))
                    resultado = validar_nota(nota)
                    if resultado is not True:
                        continue
                except ValueError:
                    print(
                        "Erro de digitação, por favor digite um número entre [0 e 10]! "
                    )
                    time.sleep(5)
                    continue
                print(update_nota(id, nota))
                cont = (
                    input("Deseja alterar outro dado do(a) aluno(a)?: [S/N]")
                    .strip()
                    .lower()
                )
                if (cont == "s") or (cont == "sim"):
                    limpartela()
                    continue
                else:
                    return "Operação cancelada!"
            case 4:
                return "Operação cancelada!"
