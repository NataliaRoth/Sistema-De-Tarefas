#Sistema de Tarefas
#Autor: Natalia Roth
from time import sleep

tarefas = []

def Linha():
    print("-" * 70)

def Espaco():
    print()

def MostrarLista():
    verlista = str(input("Antes de prosseguir, deseja ver a lista atual de tarefas (S/N)?  ")).lower()
    if verlista == "s":
        if len(tarefas) == 0:
            print("Até o momento não há tarefas cadastradas!")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i+1}. {tarefa}")
    elif verlista == "n":
        pass
    else:
        print("Escolha inválida. Tente novamente.")
        MostrarLista()


Linha()
print("Bem-vindo ao Sistema de Tarefas!".center(70))

while True:
    Linha()
    Espaco()
    sleep(1)
    print("Funções disponíveis:")
    Espaco()
    print("1. Mostrar Lista de Tarefas")
    print("2. Adicionar Tarefa")
    print("3. Editar Tarefa")
    print("4. Excluir Tarefa")
    print("5. Sair")
    Espaco()

    escolha = int(input("Escolha uma função: "))
    Espaco()
    Linha()
    sleep(1)

    if escolha == 1: #Mostrar Lista de Tarefas
        print("lista atual de tarefas:")

        if len(tarefas) == 0:
            print("Até o momento não há tarefas cadastradas!")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i+1}. {tarefa}")


    elif escolha == 2: #Adicionar Tarefa
        MostrarLista()
        Espaco()
        tarefa = str(input("Adicionar tarefa: "))
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")


    elif escolha == 3: #Editar Tarefa
        MostrarLista()
        Espaco()
        escolha = int(input("Qual a tarefa que deseja editar? ")) - 1

        if escolha < 0 or escolha > len(tarefas) -1:
            print("Escolha inválida. Essa tarefa não existe.")
            continue
        else:
            print(f"Tarefa atual: {tarefas[escolha]}")
            tarefas[escolha] = input("Editar tarefa: ")
            Espaco()
            print("Tarefa editada com sucesso!")


    elif escolha == 4: #Excluir Tarefa
        MostrarLista()
        Espaco()
        escolha = int(input("Escolha a tarefa que deseja excluir: ")) - 1

        if escolha < 0 or escolha > len(tarefas) -1:
            print("Escolha inválida. Essa tarefa não existe.")
            continue
        else:
            print(f"Tarefa escolhida: {tarefas[escolha]}")
            tarefas.pop(escolha)
            Espaco()
            print("Tarefa excluída com sucesso!")


    elif escolha == 5: #Sair
        print("Saindo do sistema...")
        break


    else: #Escolha inválida
        print("Escolha inválida. Tente novamente.")