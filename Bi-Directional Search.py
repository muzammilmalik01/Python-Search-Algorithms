# Developed by Muhammad Muzamil - https://github.com/muzammilmalik01 
# Bi-Directional Search Algorithm
from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	
	def print_list(self):
		print(self.graph)
	
	def add_edge(self,vertice,edge): #vertice is the name of the node and edge is name of node it is going to.
		self.graph[vertice].append(edge)
	
	def bidirectional_search(self,starting_vertice,ending_vertice):
		forward_queue = list() #Forward lists that keeps the record of successors.
		backward_queue = list() #Backward lists that keeps the record of predecessors.
		forward_queue.append(starting_vertice)
		backward_queue.append(ending_vertice)
		current_forward_vertice = starting_vertice #current forward
		current_backward_vertice = ending_vertice #current backward
		while current_forward_vertice != ending_vertice or current_backward_vertice != starting_vertice:
			for neighbours in self.graph[current_forward_vertice]: #gets a list of all the adjacent neighbors of successors.
				if neighbours > current_forward_vertice: #selects the node with max value value of node to traverse.
					current_forward_vertice = neighbours
					forward_queue.append(neighbours) #appends the node to the forward_queue, which is creating a path to goal node.
			for neighbours in self.graph[current_backward_vertice]: #gets a list of all the adjacent neighbors of successors.
				if neighbours < current_backward_vertice: #selects the node with min value of node to traverse.
					current_backward_vertice = neighbours 
					backward_queue.append(neighbours) #appends the node to the backward_queue, which is creating a path to staring node.
			if current_backward_vertice == current_forward_vertice: #this check helps us find the intersecting nodes.
				break #if intersecting point is found, it will come out of the while loop and will print the path.
		print("Successors Path:",forward_queue) #printing the path from starting to intersecting vertice.
		print("Predecessor Path:",backward_queue) #printing the path from goal to intersecting vertice.
		i = len(backward_queue) - 2
		while i != -1:
			forward_queue.append(backward_queue[i]) 
			i-=1
		print("Final Search Path: ",forward_queue)
		print("Frontier Node is: ",forward_queue[len(forward_queue)-1])
			
           
g = Graph() #graph 1
g2 = Graph() #graph 2
#Forward graph / Successors.
g.add_edge(0,4)
g.add_edge(1,4)
g.add_edge(2,5)
g.add_edge(3,5)
g.add_edge(4,6)
g.add_edge(5,6)
g.add_edge(6,7)
g.add_edge(7,8)
g.add_edge(8,9)
g.add_edge(8,10)
g.add_edge(9,11)
g.add_edge(9,12)
g.add_edge(10,13)
g.add_edge(10,14)

#backward graph / Predecessors.
g.add_edge(14,10)
g.add_edge(13,10)
g.add_edge(12,9)
g.add_edge(11,9)
g.add_edge(10,8)
g.add_edge(9,8)
g.add_edge(8,7)
g.add_edge(7,6)
g.add_edge(6,4)
g.add_edge(6,5)
g.add_edge(5,2)
g.add_edge(5,3)
g.add_edge(4,0)
g.add_edge(4,1)

g.bidirectional_search(0,14)
print("************************************")
print("Graph 2: ")
#Forward graph / Successors.
g2.add_edge(1,4)
g2.add_edge(2,4)
g2.add_edge(3,6)
g2.add_edge(5,6)
g2.add_edge(4,8)
g2.add_edge(6,8)
g2.add_edge(8,9)
g2.add_edge(9,10)
g2.add_edge(10,11)
g2.add_edge(10,12)
g2.add_edge(11,13)
g2.add_edge(11,14)
g2.add_edge(12,15)
g2.add_edge(12,16)

#backward graph / Predecessors.
g2.add_edge(16,12)
g2.add_edge(15,12)
g2.add_edge(13,11)
g2.add_edge(14,11)
g2.add_edge(12,10)
g2.add_edge(11,10)
g2.add_edge(10,9)
g2.add_edge(9,8)
g2.add_edge(8,4)
g2.add_edge(8,6)
g2.add_edge(6,3)
g2.add_edge(6,5)
g2.add_edge(4,2)
g2.add_edge(4,1)

# Function Call.
g2.bidirectional_search(1,15)