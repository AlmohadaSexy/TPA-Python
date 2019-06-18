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

	# A utility function to print the constructed MST stored in parent[] 
	def printMST(self, parent): 
		print("Edge \tWeight")
		for i in range(1,self.V): 
			print(parent[i],"-",i,"\t",self.mi_matriz[i][ parent[i] ] )
  
	# A utility function to find the vertex with  
	# minimum distance value, from the set of vertices  
	# not yet included in shortest path tree 
	def minKey(self, key, mstSet): 
			
		# Initilaize min value 
		min = sys.maxsize 
  
		for v in range(self.V): 
			if key[v] < min and mstSet[v] == False: 
				min = key[v] 
				min_index = v 
  
		return min_index 
  
	# Function to construct and print MST for a graph  
	# represented using adjacency matrix representation 
	def primMST(self): 
  
		#Key values used to pick minimum weight edge in cut 
		key = [sys.maxsize] * self.V 
		parent = [None] * self.V # Array to store constructed MST 
		# Make key 0 so that this vertex is picked as first vertex 
		key[0] = 0 
		mstSet = [False] * self.V 

		parent[0] = -1 # First node is always the root of 
  
		for cout in range(self.V): 
		
			# Pick the minimum distance vertex from  
			# the set of vertices not yet processed.  
			# u is always equal to src in first iteration 
			u = self.minKey(key, mstSet) 
  
            # Put the minimum distance vertex in  
            # the shortest path tree 
			mstSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
			for v in range(self.V): 
                # graph[u][v] is non zero only for adjacent vertices of m 
                # mstSet[v] is false for vertices not yet included in MST 
                # Update the key only if graph[u][v] is smaller than key[v] 
				if self.mi_matriz[u][v] > 0 and mstSet[v] == False and key[v] > self.mi_matriz[u][v]: 
					key[v] = self.mi_matriz[u][v] 
					parent[v] = u 
  
		self.printMST(parent) 

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

grafo.primMST()

grafo.imprGraph()