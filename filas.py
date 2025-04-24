class Tarefa:
    def __init__(self, descricao):
        self.descriao = descricao
        self.proxima = None

class Lista_de_Tarefas:
    def __init__(self):
        self.primeira = None
        self.ultima = None

    def esta_vazia(self):
        return self.primeira is None

    def enfileirar(self, descricao):
        novo_no = Tarefa(descricao)
        if self.esta_vazia():
            self.primeira = novo_no
            self.ultima = novo_no
        else:
            self.ultima.proxima = novo_no
            self.ultima = novo_no

    def desenfileirar(self):
        if self.esta_vazia():
            return None
        tarefa = self.primeira.descriao
        self.primeira = self.primeira.proxima
        if self.primeira is None:
            self.ultima = None
        return tarefa
    
    def ver_proxima_tarefa(self):
        return self.primeira.descriao

to_do_list = Lista_de_Tarefas()

while True:
    options = ["1 - Adicionar Nova Tarefa", "2 - Concluir próxima tarefa", "3 - Ver proxima tarefa", "4 - Sair"]
    print("Escolha uma ação")
    for option in options:
        print(option)
    
    action = input("Ação: ")

    if(action == '1'):
        descricao = input("descreva a Tarefa: ")
        to_do_list.enfileirar(descricao)

    elif(action == '2'):
        tarefa = to_do_list.desenfileirar()
        if(tarefa is not None):
            print(f'A tarefa {tarefa} foi conlcuida!')
        else:
            print('Não há tarefas para serem concluidas')

    elif(action == '3'):
        tarefa = to_do_list.ver_proxima_tarefa()
        if(tarefa is not None):
            print(f'A proxima tarefa a ser concluida é: {tarefa}')
        else:
            print("Não há tarefas para serem concluidas")

    elif(action == '4'):
        break

    else: 
        print('Ação Invalida')