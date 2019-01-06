from collections import defaultdict

global time 

class Node:
	def __init__(self,name):
		self.name = name
		self.ChildNodes = []
		self.predecessorNode = None
		self.start = 0
		self.finish = 0

def DFS(Nodes,s):
	global time
	time = 0
	for node_name in ['s','t','u', 'w', 'v', 'y', 'x', 'z']: #Nodes.keys():
		if Nodes[node_name].start==0:
			DFS_visit(Nodes,node_name)

def DFS_visit(Nodes,u):
	global time
	time = time+1
	Nodes[u].start = time
	for node_name in Nodes[u].ChildNodes:
		if Nodes[node_name].start==0:
			Nodes[node_name].predecessorNode=u
			DFS_visit(Nodes,node_name)
	time+=1
	Nodes[u].finish = time

def printPath(Nodes,u,v):
	if u==v:
		print v,
	elif Nodes[v].predecessorNode==None:
		print 'No path from soure node '+ u +' to '+ v
	else:
		printPath(Nodes,u,Nodes[v].predecessorNode)
		print v,



if __name__ == '__main__':
	## directed graph
	# GraphMap= {'u':['v','x'],'v':['y'],'w':['z'],'x':['v'],'y':'x','z':['z']}
	GraphMap= {'y':['x'],'z':['y','w'],'s':['z','w'],'x':['z'],'w':['x'],'t':['v','u'],'v':['s','w'],'u':['t','v']}
	Nodes = dict()
	for node_name in GraphMap.keys():
		 Nodes[node_name]= Node(node_name)
		 Nodes[node_name].ChildNodes=GraphMap[node_name]
	
	DFS(Nodes,'s')
	printPath(Nodes,'s','w')
	# for node_name in GraphMap.keys():
	# 	print node_name,Nodes[node_name].start,Nodes[node_name].finish





