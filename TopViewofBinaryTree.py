class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def top_view(root, m, hd,level):
    if not root:
        return 
    if hd in m:
        if level < m[hd][1]:
            m.update( {hd : [root.data,level] })
    else:
        m[hd] = [root.data,level]

    top_view(root.left, m, hd-1,level+1)
    top_view(root.right,m, hd+1, level+1)

def print_top_view(root):
    m={}
    top_view(root, m, 0, 0)

    Order = sorted(m.keys())

    for key in Order:
        print m[key][0],

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
root.left.left.left = Node(8)
root.left.left.right=Node(9)
root.left.right.left=Node(10)
root.left.right.right=Node(11)
root.right.left.left=Node(12)
root.right.left.right=Node(13)
root.right.right.left=Node(14)
root.right.right.right=Node(15)


print_top_view(root) 