import numpy as np
import sys

class Graph:
	dicc = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}
	aux = 0
	nodes = []
	def __init__(self, numNodos):
		self.V = numNodos
		self.mi_matriz = np.array([[0] * numNodos for i in range(numNodos)])

	def addArista(self, inicio, final, peso):
		if(self.exists(inicio) == False):
			noIni = Node(inicio, self.aux)
			self.addNode(noIni)
		else:
			noIni = self.getNode(inicio)
		if(self.exists(final) == False):
			noFin = Node(final, self.aux)
			self.addNode(noFin)
		else:
			noFin = self.getNode(final)
		
		self.mi_matriz[noIni.getNum(), noFin.getNum()] = peso

	def getNode(self, nombre):
		for node in self.nodes:
			if(node.getName() == nombre):
				return node

	def addNode(self, node):
		self.nodes.append(node)
		self.aux += 1

	def exists(self, nombre):
		if(self.nodes == []):
			return False
		else:
			for node in self.nodes:
				if(node.getName() == nombre):
					return True
			return False

	def imprGraph(self):
		print(self.mi_matriz)

class Node(object):
	def __init__(self, nombre, num):
		self.nombre = nombre
		self.num = num
		self.usado = False

	def setUsado(self, buleano):
		self.usado = buleano

	def getUsado(self):
		return usado

	def getNum(self):
		return self.num

	def getName(self):
		return self.nombre


grafo = Graph(6)

grafo.addArista('A', 'B', 10)
grafo.addArista('B', 'A', 10)

grafo.addArista('A', 'D', 25)
grafo.addArista('D', 'A', 25)

grafo.addArista('B', 'D', 10)
grafo.addArista('D', 'B', 10)

grafo.addArista('D', 'E', 5)
grafo.addArista('E', 'D', 5)

grafo.addArista('C', 'E', 12)
grafo.addArista('E', 'C', 12)

grafo.addArista('B', 'C', 30)
grafo.addArista('C', 'B', 30)

grafo.addArista('D', 'F', 20)
grafo.addArista('F', 'D', 20)

grafo.addArista('E', 'F', 40)
grafo.addArista('F', 'E', 40)

grafo.imprGraph()

grafo.imprGraph()