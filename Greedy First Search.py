# Developed by Muhammad Muzamil - https://github.com/muzammilmalik01 
# Greedy Best First Search. 
# Heuiristic Value: Node Cost.
from collections import defaultdict
import heapq

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
		self.nodecost = defaultdict(list)
	
	def print_list(self):
		print(self.graph)
	
	def add_edge(self,vertice,edge,hcost): #vertice is the name of the node and edge is name of node it is going to.
		self.nodecost = [edge,hcost]
		self.graph[vertice].append(self.nodecost)
		
	def greedy_first_search(self,start_node,end_node):
		queue = []
		visited = []
		found = False
		heapq.heappush(queue,(0,start_node))
		while  not found:
			node = heapq.heappop(queue)#get the node with minimum cost
			print('Poped: ',node[1],' with the min node cost of ',node[0],'\n')
			node = node[1] 
			visited.append(node)
			for neighbors in self.graph[node]:#get all the neighbours of the min-cost node.
				heapq.heappush(queue,(neighbors[1],neighbors[0]))#push them to the queue.
				if neighbors[0] == end_node: #if the node is found, while loop will break.
					print('The Required node ', neighbors[0], ' has been found.\n')
					visited.append(end_node)
					found = True
					break
			print('Priority Queue: ',queue)
		# After the while loop in the greedy_first_search method
		if not found and len(queue) == 0:
			print('The goal node', end_node, 'cannot be reached from the start node', start_node)

            
g = Graph()
#g.add_edge('Node','Neighbouring Node','Value/Cost of the neighbouring Node')
g.add_edge('S','A',11)
g.add_edge('S','B',8)
g.add_edge('S','C',5)
g.add_edge('A','D',9)
g.add_edge('A','E',14)
g.add_edge('B','F',12)
g.add_edge('B','G',13)
g.add_edge('C','H',7)
g.add_edge('H','I',4)
g.add_edge('H','J',6)
g.add_edge('I','K',8)
g.add_edge('I','L',9)
g.add_edge('I','M',10)
# g.print_list()
g.greedy_first_search('S','I')