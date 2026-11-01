#Sistema de Tarefas
#Autor: Natalia Roth
from time import sleep
import questionary

tarefas = []

# Função para imprimir uma linha de separação
def Linha():
    print("-" * 70)

# Função para imprimir uma linha em branco
def Espaco():
    print()

# Dicionário para mapear as prioridades para valores numéricos
ORDEM_PRIORIDADE = {
    '\U0001F534 Alta': 0,
    '\U0001F7E1 Moderada': 1,
    '\U0001F7E2 Leve': 2,
}

# Função para ordenar a lista de tarefas com base na prioridade
def OrdenarTarefas():
    tarefas.sort(key=lambda t: ORDEM_PRIORIDADE.get(t[1], 99))

# Função para exibir a lista de tarefas, mostrando a prioridade junto com a tarefa
def ExibirTarefas():
    if len(tarefas) == 0:
        print("Até o momento não há tarefas cadastradas!")
    else:
        print("Lista de tarefas organizada por prioridade:")
        Espaco()
        OrdenarTarefas()
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1}. {tarefa[1]} - {tarefa[0]}")  # Mostrar prioridade junto com a tarefa

# Função para mostrar a lista de tarefas, dependendo da escolha do usuário
def MostrarLista():
    if escolha == 1: #Se o usuário escolheu a função de mostrar a lista, não perguntar se quer ver a lista
        ExibirTarefas()
    else:  #Se o usuário escolheu outra função, perguntar se quer ver a lista antes de prosseguir
        while True:
            verlista = str(input("Antes de prosseguir, deseja ver a lista atual de tarefas (S/N)?  ")).lower()
            if verlista == "s":
                ExibirTarefas()
                break
            elif verlista == "n":
                break
            else:
                print("Escolha inválida. Tente novamente.")

# Função para adicionar prioridade a uma tarefa
def Prioridades(): # TESTE TESTE TESTe para adc prioridades
    prioridade = questionary.select("Qual a prioridade desta tarefa? ",
        choices=list(ORDEM_PRIORIDADE.keys())
    ).ask()
    return prioridade

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

    try: # Pegar a escolha do usuário e tratar erros de digitação
        escolha = int(input("Escolha uma função: "))
    except ValueError:
        print("valor inválido. Tente novamente.") 
        continue

    Espaco()
    Linha()
    sleep(1)

    if escolha == 1: #Mostrar Lista de Tarefas
        MostrarLista()


    elif escolha == 2: #Adicionar Tarefa
        MostrarLista()
        Espaco()
        
        tarefa = str(input("Adicionar tarefa: "))
        prioridade = Prioridades() # Chamar a função Prioridades para o usuário escolher a prioridade da tarefa
        tarefas.append((tarefa, prioridade))
        print("Tarefa adicionada com sucesso!")


    elif escolha == 3: #Editar Tarefa
        MostrarLista()
        Espaco()

        while True:
            try: # Pegar a escolha do usuário e tratar erros de digitação
                escolha = int(input("Qual a tarefa que deseja editar? ")) - 1
                if escolha < 0 or escolha >= len(tarefas):
                    raise IndexError
                break
            except ValueError:
                print("Valor digitado é inválido. Tente novamente.")
            except IndexError:
                print("Escolha inválida. Essa tarefa não existe.")

        # Pegar a escolha do usuário e informar a tarefa atual, pedir para editar a tarefa e informar que foi sucesso
        print(f"Tarefa a modificar: {tarefas[escolha]}")
        Espaco()
        escolhaTarefa = input("Novo nome da tarefa: ")
        escolhaPrioridade = Prioridades() # Adicionar prioridade junto com a tarefa
        tarefas[escolha] = [escolhaTarefa, escolhaPrioridade]
        Espaco()
        print("Tarefa editada com sucesso!")


    elif escolha == 4: #Excluir Tarefa
        MostrarLista()
        Espaco()

        while True:
            try: # Pegar a escolha do usuário e tratar erros de digitação
                escolha = int(input("Escolha a tarefa que deseja excluir: ")) - 1
                if escolha < 0 or escolha >= len(tarefas):
                    raise IndexError
                break
            except ValueError:
                print("Valor digitado é inválido. Tente novamente.")
            except IndexError:
                print("Escolha inválida. Essa tarefa não existe.")
    
        # Pegar a escolha do usuário e informar a tarefa atual, pedir para confirmar a exclusão da tarefa e informar que foi sucesso
        print(f"Tarefa escolhida: {tarefas[escolha]}")
        tarefas.pop(escolha)
        Espaco()
        print("Tarefa excluída com sucesso!")       


    elif escolha == 5: #Sair
        print("Saindo do sistema...")
        break


    else: #Escolha inválida
        print("Escolha inválida. Tente novamente.")