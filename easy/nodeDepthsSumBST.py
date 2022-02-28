def nodeDepths(root):
	s=[]
	bfs(root,s)
	return sum(s)

def bfs(root,s,depth=0):
	if not root:
		return
	s.append(depth)
	bfs(root.left,s,depth+1)
	bfs(root.right,s,depth+1)
	
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None