#kutty's playground

def minHeightBst(array,root = None):
	if len(array) ==0:
		return
	mid = len(array)//2
	if root is None:
		root = BST(array[mid])
	else:
		root.insert(array[mid])
	minHeightBst(array[:mid],root)
	minHeightBst(array[mid+1:],root)
	return root

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
