from tabulate import tabulate
lista_alunos = []
id = 1
def adicionar_aluno():
    global id
    nome = input("DIGITE O NOME E SOBRENOME DO ALUNO: ").strip().upper()
    ano_nsc = int(input(f"QUAL É O ANO DE NASCIMENTO DO ALUNO(A) {nome}: "))
    nota = float(input(f"QUAL FOI A NOTA DO(A) {nome}: "))
    tabela = {
    "ID" : id,   
    "Nome Do Aluno" : nome,
    "Ano De Nascimento Do Aluno(A)" : ano_nsc,
    "Nota Do Aluno(A)" : nota
}
    lista_alunos.append(tabela)
    id += 1
    print("Aluno adicionado com sucesso!\n")

def listar_alunos():
    print("\n" + "="*85)
    print(f"{'ID':<5} | {'NOME DO ALUNO':<30} | {'ANO NASC.':<10} | {'NOTA':<6}")
    print("="*85)
    for aluno in lista_alunos:
        id_aluno = aluno.get("ID", "-")
        nome = aluno.get("Nome Do Aluno", "Não Informado")
        ano = aluno.get("Ano De Nascimento Do Aluno(A)", 0)
        nota = aluno.get("Nota Do Aluno(A)", 0.0)
        print(f"{id_aluno:<5} | "
            f"{nome:<30} | "
            f"{ano:<10} | "
            ,f"{nota:<6.1f}")
        
    print("="*85 + "\n")

    


def media_turma():
    md = 0
    if len(lista_alunos) == 0:
        return "NAO HÁ ALUNOS REGISTRADOS"
    soma = 0
    for aluno in lista_alunos:
        soma += aluno['Nota Do Aluno(A)']
    md = soma / len(lista_alunos)
    return f"A MEDIA DA TURMA É {md:.2f}"

def remover_aluno():
    remover = input("QUAL ALUNO DESEJA REMOVER: ").strip().upper()
    for aluno in lista_alunos:
        if aluno["Nome Do Aluno"] == remover:
            lista_alunos.remove(aluno)
            return f"Aluno:{remover} REMOVIDO COM SUCESSO"
    else:
        return f"Aluno:{remover} NAO EXISTE"

def buscar():
    busca = input("QUAL ALUNO DESEJA PROCURAR: ").strip().upper()
    for aluno in lista_alunos:
        if aluno["Nome Do Aluno"] == busca:
            return f"Aluno:{busca} ENCONTRADO/A"
    else:
        return f"Aluno:{busca} NAO FOI ENCONTRADO/A"