class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root,res=[],s=0):
	res=[]
	bfs(root,res)
	return res

def bfs(root,res,s=0):
	if not root:
		return
	if not root.left and not root.right:
		res.append(s+root.value)
		
	bfs(root.left,res,s+root.value)
	bfs(root.right,res,s+root.value)