from collections import defaultdict

class Node:
	def __init__(self,name):
		self.name = name
		self.adjecentNodes = []
		self.predecessorNode = None
		self.distance = 0


## breadth first search with source vertex s
def BFS(Nodes,s):
	Queue = []
	visted = defaultdict(lambda:0)

	## mark the source vertex s as visted and enqueue it
	Queue.append(s)
	visted[s]=1

	while Queue:
		print Queue
		u = Queue.pop(0)		
		
		AdjNodes = Nodes[u].adjecentNodes ## node name
		for node_name in AdjNodes:
			if visted[node_name]==0: 				
				visted[node_name]=1
				Nodes[node_name].predecessorNode = u
				Nodes[node_name].distance = Nodes[u].distance+1
				Queue.append(node_name)

def printPath(Nodes,u,v):
	if u==v:
		print v,
	elif Nodes[v].predecessorNode==None:
		print 'No path from soure node '+ u +' to '+ v
	else:
		printPath(Nodes,u,Nodes[v].predecessorNode)
		print v,


if __name__ == '__main__':
	GraphMap= {'s':['w','r'],'r':['v','s'],'t':['w','x','u'],'u':['t','x','y'],'v':['r'],'w':['s','t','x'],'x':['w','t','u','y'],'y':['x','u']}
	Nodes = dict()
	for node_name in GraphMap.keys():
		 Nodes[node_name]= Node(node_name)
		 Nodes[node_name].adjecentNodes=GraphMap[node_name]

	BFS(Nodes,'s')
	printPath(Nodes,'s','y')
	print Nodes['y'].distance




	





