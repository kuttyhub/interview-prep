#kutty's playground

def invertBinaryTree(tree):
	if tree is None:
		return
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)
	swapNodes(tree)

def swapNodes(tree):
	if tree is None:
		return 
	tree.left,tree.right  = tree.right,tree.left

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

