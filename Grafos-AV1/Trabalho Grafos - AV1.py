import math

import matplotlib.pyplot as plt

class Vertice:
    def __init__(self, dado):
        self.dado = dado
        self.conectados = []
        self.grau = 0

class Aresta:
    def __init__(self, vertice1, vertice2):
        self.vertice1 = vertice1
        self.vertice2 = vertice2

class Grafo:
    def __init__(self, dados, vizinhos):
        self.maiorGrau = 0
        self.menorGrau = math.inf
        self.V = []
        self.E = []
        self.MA = [] # Matriz de Adjacência
        self.MI = [] # Matriz de Incidência
        self.LI = [] # Lista Indexada
        for dado in dados:
            verticeAdd = Vertice(dado)
            for vizinho in vizinhos:
                if dado == vizinho[0]:
                    verticeAdd.conectados.append(vizinho[1])
                elif dado == vizinho[1]:
                    verticeAdd.conectados.append(vizinho[0])
            self.V.append(verticeAdd)
        for vizinho in vizinhos:
            for i in range(0, len(self.V)):
                if self.V[i].dado == vizinho[0] and self.V[i].dado == vizinho[1]:
                    aresta= Aresta(self.V[i],self.V[i])
                    self.E.append(aresta)
                    self.V[i].grau+=1
                    continue
                elif self.V[i].dado ==vizinho[0]:
                    dadoProcurado = vizinho[1]
                elif self.V[i].dado == vizinho[1]:
                    dadoProcurado = vizinho[0]
                else:
                    continue
                for j in range(i+1, len(self.V)):
                    if self.V[j].dado == dadoProcurado:
                        aresta = Aresta(self.V[i], self.V[j])
                        self.E.append(aresta)
                        self.V[i].grau += 1
                        self.V[j].grau += 1
        for vertice in self.V:
            if vertice.grau > self.maiorGrau:
                self.maiorGrau = vertice.grau
            if vertice.grau < self.menorGrau:
                self.menorGrau = vertice.grau
        self.matrizDeAdjacencia()
        self.matrizDeIncidencia()
        self.listaIndexada()

    def exibirGraus(self):
        maior = []
        menor = []
        for vertice in self.V:
            if vertice.grau == self.maiorGrau:
                maior.append(vertice.dado)
            if vertice.grau == self.menorGrau:
                menor.append(vertice.dado)
        print(f"Maior(es) Grau(s): {maior}")
        print(f"Menor(es) Grau(s): {menor}")

    def matrizDeAdjacencia(self):
        for vertice in self.V:
            linha = []
            for vertice2 in self.V:
                if vertice.dado in vertice2.conectados or vertice2.dado in vertice.conectados:
                    linha.append(1)
                else:
                    linha.append(0)
            self.MA.append(linha)

    def exibirMA(self):
        for linha in self.MA:
            print(linha)

    def matrizDeIncidencia(self):
        for vertice in self.V:
            linha = []
            for aresta in self.E:
                if vertice.dado == aresta.vertice1.dado or vertice.dado == aresta.vertice2.dado:
                    linha.append(1)
                else:
                    linha.append(0)
            self.MI.append(linha)

    def exibirMI(self):
        for linha in self.MI:
            print(linha)

    #Lista indexada
    def listaIndexada(self):
        alfa = []
        indice=0 #indice do primeiro vértice
        alfa.append(indice)
        beta = []
        # alfa
        for i in range(0, len(self.V)):
            indice += (self.V[i].grau)
            alfa.append(indice)
        #beta
        for i in range(0,len(self.V)+1):
            if i==len(self.V):
                beta.append([])
                break
            for conectado in self.V[i].conectados:
                beta.append(conectado)
        self.LI.append([alfa, beta])
    def exibirLI(self):
        for item in self.LI:
            print(item)

    def addV(self, vertice):
        self.V.append(vertice)
        return vertice

    def addE(self, v1, v2):
        self.E.append(Aresta(v1, v2))

        #histograma

    def plot_histograma(self):
        dadosX = [vertice.dado for vertice in self.V]
        dadosY = [vertice.grau for vertice in self.V]
        plt.bar(dadosX, dadosY,align="center")
        plt.xlabel('Vértices')
        plt.ylabel('Grau dos Vértices')
        plt.title('Histograma de Grau dos Vértices')
        plt.yticks(range(0, self.maiorGrau + 1))
        plt.grid(True)
        plt.show()

# Exemplo do Trabalho
estados = ["AC","AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
fronteiras = [["AC","AM"],["AL","BA"],["AL","SE"],["AL","PE"],["AP","PA"],["AM","RO"],["AM","RR"],["AM","PA"],["BA","SE"],["BA","PE"],["BA","PI"],["BA","TO"],["BA","GO"],["BA","MG"],["BA","ES"],["CE","RN"],["CE","PB"],["CE","PE"],["CE","PI"],["DF","GO"],["DF","MG"],["ES","MG"],["ES","RJ"],["G0","MG"],["GO","TO"],["GO","MT"],["GO","MS"],["MA","PI"],["MA","TO"],["MA","PA"],["MT","RO"],["MT","MS"],["MT","TO"],["MT","PA"],["MS","PR"],["MS","SP"],["MG","SP"],["MG","RJ"],["PA","TO"],["PA","RR"],["PB","RN"],["PB","PE"],["PR","SP"],["PR","SC"],["PE","PI"],["PI","TO"],["RJ","SP"],["RS","SC"]]

grafo = Grafo(estados, fronteiras)
print("Matriz de Adjacência:")
grafo.exibirMA()
print("Matriz de Incidência:")
grafo.exibirMI()
print("Lista Indexada:")
grafo.exibirLI()
grafo.exibirGraus()
print(f"Valor do Maior Grau:{grafo.maiorGrau}")
print(f"Valor do Menor Grau:{grafo.menorGrau}")
grafo.plot_histograma()


