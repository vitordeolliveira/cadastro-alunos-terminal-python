import os
def limpartela():
    os.system('cls' if os.name == 'nt' else 'clear')

def media_turma():
    limpartela()
    if len(lista_alunos) == 0:
        print("NAO HÁ ALUNOS REGISTRADOS")
        return None
    soma = 0
    for aluno in lista_alunos:
        soma += aluno['Nota Do Aluno']
    return soma / len(lista_alunos)


def adicionar_aluno(nome):
    idade_ = int(input(f"QUAL É A IDADE DO/A {nome}: "))
    nota_ = float(input(f"QUAL FOI A NOTA DO/A {nome}: "))
    dicionario_escolar = {
    "Nome Do Aluno":nome,
    "Idade Do Aluno":idade_,
    "Nota Do Aluno":nota_
}
    lista_alunos.append(dicionario_escolar)
    

print("--------------------------")
print("===ESCOLA MUNICIPAL===")
print("--------------------------")
lista_alunos = []
while True:
    print("\n1 = ADICIONAR ALUNO\n2 = LISTAR TODOS OS ALUNOS\n3 = BUSCAR ALUNO PELO NOME\n4 = REMOVER ALUNO\n5 = MOSTRAR MEDIA GERAL DA TURMA\n6 = SAIR\n")
    valor = int(input("OPCAO DESEJADA:"))
    match valor:
        case 1:
           nome_ = input("DIGITE O NOME DO ALUNO: ").strip().upper()
           adicionar_aluno(nome_)
        case 2:
            limpartela()
            for alunos in lista_alunos:
                print(alunos)

        case 3:
            limpartela()
            busca_aluno = input("QUAL ALUNO DESEJA PROCURAR: ").strip().upper()
            for aluno in lista_alunos:
                if aluno["Nome Do Aluno"] == busca_aluno:
                    print(aluno)
                    break    
                else:
                    print(f"O ALUNO/A {busca_aluno} NAO FOI ENCONTRADO/A")
                    break         
        case 4:
            limpartela()
            remover_aluno = input("QUAL ALUNO DESEJA REMOVER: ").strip().upper()
            for aluno in lista_alunos:
                if aluno["Nome Do Aluno"] == remover_aluno:
                    lista_alunos.remove(aluno)
                    print(f"Aluno {aluno} REMOVIDO COM SUCESSO")
                    break
            else:
                print(f"O ALUNO/A {remover_aluno} NAO EXISTE")
        case 5:
                media = media_turma()
                if media is None:
                    continue
                else:
                    print(f"A MEDIA DA TURMA É {media:.2f}")
        case 6:
            break
        case _:
            break