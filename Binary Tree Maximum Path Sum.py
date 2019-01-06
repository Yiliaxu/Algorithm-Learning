class TreeNode:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None


def GenerateBinaryTree(InputValue):
	TreeRoot = TreeNode(InputValue[0])
	NodeQueue = [TreeRoot]
	i = 1
	front = 0
	while i<len(InputValue):
		node = NodeQueue[front]
		front+=1
		if InputValue[i]!='null':
			node.left = TreeNode(InputValue[i])
			NodeQueue.append(node.left)
		i+=1
		if i>=len(InputValue):
			break
		if InputValue[i]!='null':
			node.right = TreeNode(InputValue[i])
			NodeQueue.append(node.right)
		i+=1
	return TreeRoot



def FindMaxUtil(root):
	global res

	if not root:
		return 0

	LeftMax = FindMaxUtil(root.left)
	RightMax = FindMaxUtil(root.right)

	max_single = max([root.value,max([LeftMax,RightMax])+root.value])
	max_subtree = max([max_single,LeftMax+RightMax+root.value])

	res = max([res,max_subtree])

	return max_single 



if __name__ == '__main__':
	InputValue=[1,2,3,4,5,'null',6,'null',7,'null','null',8,'null','null',9,'null','null','null',10]
	root = GenerateBinaryTree(InputValue)
	global res
	res = -10000
	FindMaxUtil(root)
	print res
 