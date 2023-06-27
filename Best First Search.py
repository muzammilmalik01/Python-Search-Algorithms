# Developed by Muhammad Muzamil - https://github.com/muzammilmalik01 
# Best First Search. 
# Heuiristic Value: Edge Cost.
from collections import defaultdict
import heapq

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
		self.edgecost = defaultdict(list)
	
	def print_list(self):
		print(self.graph)
	
	def add_edge(self,vertice,edge,edgecost): #vertice is the name of the node and edge is name of node it is going to.
		self.Edge = [edge,edgecost]
		self.graph[vertice].append(self.Edge)
		
	def best_first_search(self,start_node,end_node):
		queue = []
		visited = []
		found = False
		heapq.heappush(queue,(0,start_node))
		while not found:
			node = heapq.heappop(queue)#get the node with minimum cost
			print('Poped: ',node[1],' with the min edge cost of ',node[0],'\n')
			node = node[1] 
			visited.append(node)
			for neighbors in self.graph[node]:#visit neighbours of the min node and add them to the queue. 
				heapq.heappush(queue,(neighbors[1],neighbors[0]))
				if neighbors[0] == end_node: # if the end/ goal node has been found, the search will end.
					print('The goal node ',end_node,' has been found.\n')
					visited.append(end_node)
					found = True
					break
			print('Priority Queue: ',queue)
		if not found:
			print('The goal node', end_node, 'cannot be reached from the start node', start_node)

g = Graph()
g.add_edge('S','A',3)
g.add_edge('S','B',6)
g.add_edge('S','C',5)
g.add_edge('A','D',9)
g.add_edge('A','E',8)
g.add_edge('B','F',12)
g.add_edge('B','G',14)
g.add_edge('C','H',7)
g.add_edge('H','I',5)
g.add_edge('H','J',6)
g.add_edge('I','K',1)
g.add_edge('I','L',10)
g.add_edge('I','M',2)

# Funtion Call.
g.best_first_search('S','I')