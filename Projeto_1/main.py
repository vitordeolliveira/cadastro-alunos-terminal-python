from visual import menu

lista_alunos = []
while True:
    menu.limpartela()
    valor = menu.tabela()
    match valor:
        case 1:
           menu.adicionar_aluno()
        case 2:
            menu.limpartela()
            for alunos in lista_alunos:
                print(alunos["Nome Do Aluno"])

        case 3:
            print (menu.buscar())      
        case 4:
            print (menu.remover_aluno())
        case 5:
            print (menu.media_turma())
        case _:
            break