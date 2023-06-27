# Developed by Muhammad Muzamil - https://github.com/muzammilmalik01 
# Travelling Sales Man. 
# Heuiristic Value: Nearest Neighbor.
# Confirmation: https://cbom.atozmath.com/CBOM/Assignment.aspx?q=tsnn&q1=x%2c180%2c195%2c207%2c274%3b180%2cx%2c200%2c212%2c240%3b195%2c200%2cx%2c220%2c230%3b207%2c212%2c220%2cx%2c225%3b274%2c240%2c230%2c225%2cx%60MIN%60A%2cB%2cC%2cD%2cE%60A%2cB%2cC%2cD%2cE%60false%60false&do=1#PrevPart
from collections import defaultdict
import heapq

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
		self.edgecost = defaultdict(list)
	
	def printList(self):
		print(self.graph)
	
	def addEdge(self,vertice,edge,edgecost): #vertice is the name of the node and edge is name of node it is going to.
		self.Edge = [edge,edgecost]
		self.graph[vertice].append(self.Edge)
		
	def TSM(self,starting_node,states): #Parameters: Starting Node, Total number of States.
		visited = list()
		queue = []
		current_node = starting_node
		complete = False
		cost = 0
		print('Path: ',current_node,' -> ', end = '')
		while complete == False:
			for neighbors in self.graph[current_node]:#Getting all neighbors of the node.
				heapq.heappush(queue,[neighbors[1], neighbors[0]]) #Pushing nodes according to smallest path.
			for i in queue:#selecting the best unvisited node. (Smallest Path Node)
				if i[1] not in visited:
					if len(visited) < states - 1 and i[1] != starting_node: #Unvisited Nodes Selection.
						current_node = i[1]
						visited.append(i[1])
						print(i[1],' -> ',end= '')
						cost += int(i[0])
						break
					elif len(visited) == states - 1 and i[1] == starting_node:#Traversing back to Start Node.
						visited.append(i[1])
						cost += int(i[0])
						print(i[1])
						break
			queue.clear()
			if len(visited) == states:
				complete = True
		print('Minimal Cost: ',cost)
#Setting up the graph.
g = Graph()
g.addEdge('A','B',180)
g.addEdge('A','C',195)
g.addEdge('A','D',207)
g.addEdge('A','E',274)

g.addEdge('B','A',180)
g.addEdge('B','C',200)
g.addEdge('B','D',212)
g.addEdge('B','E',240)

g.addEdge('C','A',195)
g.addEdge('C','B',200)
g.addEdge('C','D',220)
g.addEdge('C','E',230)

g.addEdge('D','A',207)
g.addEdge('D','B',212)
g.addEdge('D','C',220)
g.addEdge('D','E',225)

g.addEdge('E','A',274)
g.addEdge('E','B',240)
g.addEdge('E','C',230)
g.addEdge('E','D',225)

#Calling the Algo.
g.TSM('D',5)