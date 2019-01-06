from collections import defaultdict
from collections import deque


class TreeNode:
	def __init__(self,x):
		self.value=x
		self.right = None
		self.left = None

    ##### depth first search
	def rightSideViewDepth(self, root):
		rightmost_value_at_depth = dict() # depth -> node.val
		max_depth = -1

		stack = [(root, 0)]
		while stack:
			node, depth = stack.pop()

			if node is not None:
				# maintain knowledge of the number of levels in the tree.
				max_depth = max(max_depth, depth)

				# only insert into dict if depth is not already present.
				rightmost_value_at_depth.setdefault(depth, node.value)

				stack.append((node.left, depth+1))
				stack.append((node.right, depth+1))

		return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]


	### breadth first search
	def rightSideViewBreath(self, root):
		rightmost_value_at_depth = dict() # depth -> node.val
		max_depth = -1

		queue = deque([(root, 0)])
		while queue:
			node, depth = queue.popleft()

			if node is not None:
				# maintain knowledge of the number of levels in the tree.
				max_depth = max(max_depth, depth)

				# overwrite rightmost value at current depth. the correct value
				# will never be overwritten, as it is always visited last.
				rightmost_value_at_depth[depth] = node.value

				queue.append((node.left, depth+1))
				queue.append((node.right, depth+1))

		return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]

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



# Recursive function to print right view of Binary Tree
# used max_level as reference list ..only max_level[0] 
# is helpful to us
def rightViewUtil(root, level, max_level):
     
    # Base Case
    if root is None:
        return
     
    # If this is the last node of its level
    if (max_level[0] < level):
        print "%d   " %(root.value),
        max_level[0] = level
 
    # Recur for right subtree first, then left subtree
    rightViewUtil(root.right, level+1, max_level)
    rightViewUtil(root.left, level+1, max_level)
 
def rightView(root):
    max_level = [0]
    rightViewUtil(root, 1, max_level)



if __name__ == '__main__':
	# InputValue=[7,4,11,3,6,9,18,2,'null','null','null','null','null',14,3]
	InputValue=[1,2,3,4,5,'null',6,'null',7,'null','null',8,'null','null',9,'null','null','null',10]
	TreeRoot = GenerateBinaryTree(InputValue)
	RightViewList =TreeRoot.rightSideViewDepth(TreeRoot)
	print RightViewList
	rightView(TreeRoot)
	RightViewList =TreeRoot.rightSideViewBreath(TreeRoot)
	print RightViewList


	

