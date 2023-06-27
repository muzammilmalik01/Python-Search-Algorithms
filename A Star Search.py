# Developed by Muhammad Muzamil - https://github.com/muzammilmalik01 
# A* Search. 
# Heuiristic Value: Edge Cost + Node Cost.
from collections import defaultdict
import heapq

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
		self.edge_cost = defaultdict(list)
		self.node_cost = defaultdict(list)
	
	def print_list(self):
		print(self.graph)
	
	def add_edge(self,vertice,edge,edge_cost): #vertice is the name of the node and edge is name of node it is going to.
		self.Edge = [edge,edge_cost]
		self.graph[vertice].append(self.Edge)

	def set_node_cost(self,n,nc): #setting the cost of the nodes.
		self.node_cost[n].append(nc)
		

	def a_star_search(self, start_node, end_node):
		queue = []
		visited = []
		found = False
		heapq.heappush(queue, (0, start_node))
		while not found and queue:
			node = heapq.heappop(queue)
			node_cost = node[0]
			node = node[1]
			visited.append(node)
			if node == end_node:
				print('The goal node', end_node, 'has been found.')
				visited.append(end_node)
				found = True
				break
			for neighbors in self.graph[node]:
				neighbor_node = neighbors[0]
				neighbor_edge_cost = neighbors[1]
				neighbor_heuristic_cost = self.node_cost[neighbor_node][0]
				total_cost = node_cost + neighbor_edge_cost + neighbor_heuristic_cost
				if neighbor_node not in visited:
					heapq.heappush(queue, (total_cost, neighbor_node))
		
		if not found:
			print('The goal node', end_node, 'cannot be reached from the start node', start_node)
		
		print('Visited nodes:', visited)

	
            
g = Graph()
#g.add_edge('Node','Neighbouring Node','Value/Cost of the edge to the other node, Node Heuristic Cost')
g.add_edge('S','A',10)
g.add_edge('S','B',7)
g.add_edge('S','C',4)
g.add_edge('A','D',8)
g.add_edge('A','E',13)
g.add_edge('B','F',11)
g.add_edge('B','G',12)
g.add_edge('C','H',6)
g.add_edge('H','I',3)
g.add_edge('H','J',5)
g.add_edge('I','K',7)
g.add_edge('I','L',8)
g.add_edge('I','M',9)

#setting Heuristic Node Costs.
g.set_node_cost('S',19)
g.set_node_cost('A',11)
g.set_node_cost('B',8)
g.set_node_cost('C',5)
g.set_node_cost('D',9)
g.set_node_cost('E',14)
g.set_node_cost('F',12)
g.set_node_cost('G',13)
g.set_node_cost('H',7)
g.set_node_cost('I',4)
g.set_node_cost('J',6)
g.set_node_cost('K',8)
g.set_node_cost('L',9)
g.set_node_cost('M',10)

# function calling
g.a_star_search('S','I')