import sys, numpy

class Grafo:
	def __init__(self, numNodos):
		"""
		Constructor de la clase grafo

		Le metemos como dato la cantidad de vertices que va a haber y nos crea una matriz cuadrada que usaremos como nuestro grafo
		"""
		self.vertices = numNodos
		self.grafo = numpy.array([[0] * self.vertices for i in range(self.vertices)])
		self.finalCamino = []
	
	def addEdge(self, inicio, fin, peso):
		"""
		Añadimos una arista con su peso

		Al ser un grafo dirigido, tenemos que tener cuidado con el inicio y el final de cada arista

		En el grafo cambiamos el 0 por el peso en las coordenadas [inicio, fin]
		"""
		self.grafo[inicio][fin] = peso
		self.grafo[fin][inicio] = peso

	def minimaDistancia(self):
		"""
		Miramos todos los vertices a los que se puede llegar desde cada vertice y devolvemos el menor indice de cada uno
		"""
		minim = sys.maxsize 
		minim_index = -1

		for v in range(0, self.vertices):
			if(self.cogidos[v] == False and self.distancias[v] <= minim):
				minim = self.distancias[v]
				minim_index = v

		return minim_index

	def imprimirDistancias(self, inicio, final):
		"""
		Imprimimos lo que cuesta en llegar de inicio a fin, y si no se puede llegar ponemos un mensaje de error
		"""
		fin = self.distancias[final]
		if(fin == sys.maxsize):
			print(f'No se puede llegar hasta el nodo {final} desde {inicio}')
		else:
			print(f'Camino de {inicio} a {final} pesa {fin}')

		self.representarCamino(final)
		print(f'El camino final es {self.finalCamino}')

	def representarCamino(self, curr):
		if(curr == -1):
			return
		self.representarCamino(self.camino[curr])
		self.finalCamino.append(curr)

	def dijkstra(self, inicio, final):
		"""
		encontramos la distancia minima de un nodo a otro con el menor coste
		"""
		self.distancias = []
		self.cogidos = []
		self.camino = [0] * self.vertices
		self.camino[inicio] = -1

		for x in range(0, self.vertices):
			self.distancias.append(sys.maxsize)
			self.cogidos.append(False)

		self.distancias[inicio] = 0

		for cont in range(0, self.vertices - 1):
			i = self.minimaDistancia()
			self.cogidos[i] = True

			for j in range(0, self.vertices):
				if(self.cogidos[j] == False and self.grafo[i][j] != 0 and self.distancias[i] != sys.maxsize and self.distancias[i] + self.grafo[i][j] < self.distancias[j]):
					self.camino[j] = i
					self.distancias[j] = self.distancias[i] + self.grafo[i][j]

		self.imprimirDistancias(inicio, final)

"""g = Grafo(10)

g.addEdge(0, 4, 1)
g.addEdge(0, 7, 10)
g.addEdge(1, 2, 2)
g.addEdge(3, 0, 4)
g.addEdge(3, 7, 1)
g.addEdge(4, 5, 3)
g.addEdge(5, 1, 1)
g.addEdge(5, 2, 3)
g.addEdge(5, 6, 7)
g.addEdge(5, 8, 1)
g.addEdge(7, 4, 5)
g.addEdge(7, 8, 9)
g.addEdge(8, 9, 2)
g.addEdge(9, 6, 1)"""

g = Grafo(9);
g.addEdge(0,1,25);
g.addEdge(0,3,50);
g.addEdge(0,8,46);

g.addEdge(1,2,18);
g.addEdge(1,4,42);
g.addEdge(1,7,49);

g.addEdge(2,4,28);
g.addEdge(2,5,50);
g.addEdge(2,7,39);

g.addEdge(3,4,20);
g.addEdge(3,6,48);

g.addEdge(4,5,55);

g.addEdge(5,6,9);
g.addEdge(5,7,37);

g.addEdge(6,8,43);

g.addEdge(7,8,20);

#'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9
print(g.grafo)
g.dijkstra(0, 6)