#Classe pagina
class Pagina():
    def __init__(self, endereco):
        self.endereco = endereco #Endereço da pagina
        self.proxima = None #Pagina seguinte

#Classe historico de pesquisa
class Historico_de_pesquisa():
    def __init__(self):
        self.ultima = None #Pagina no topo da pilha
        self.total = 0 #total de paginas da pilha

    def visitar_pagina(self, endereco):
        nova_pagina = Pagina(endereco) #Instancia uma nova pagina
        nova_pagina.proxima = self.ultima #Nova pagina aponta para a ultima pagina do historico
        self.ultima = nova_pagina #Define a nova pagina como ultima do historico
        self.total += 1 #Atualiza quantidade de paginas no historico

    def voltar(self):
        pagina_removida = self.ultima.endereco #Obtem o endereço da pagina no topo da lista
        self.ultima = self.ultima.proxima #Define a pagina anterior como ultima do historico
        self.total -= 1 #Atualiza quantidade de paginas do historico
        return pagina_removida #retorna pagina removida do historico

    def exibir_historico(self):
        atual = self.ultima #Obtém a ultima pagina do historico
        while atual is not None: #Exibe as paginas do historico
            print(atual.endereco)
            atual = atual.proxima

    def pagina_atual(self):
        print(self.ultima.endereco) #exibe pagina no topo do historico

historico = Historico_de_pesquisa()

historico.visitar_pagina('https://www.bing.com/') #Adicona pagina do Bing ao histoirco de pesquisas
historico.visitar_pagina('https://github.com/') #Adiciona pagina do github ao historico de pesquisas
historico.visitar_pagina('https://www.cps.sp.gov.br/fatecs/fatec-jundiai-deputado-ary-fossen/') #Adiciona pagina da Fatec ao historico de pesquisas

print('Historico de navegação')
historico.exibir_historico() #exibe historico de pesquisa contendo as tres paginas

print('Voltando à pagina aterior')
print(historico.voltar()) #considerando que a pagina da fatec é a ultima da fila, retorna à pagina do github e exclui a pagina da fatec da pilha

print('Historico Atualizado')
historico.exibir_historico() #exie historico contendo as duas paginas