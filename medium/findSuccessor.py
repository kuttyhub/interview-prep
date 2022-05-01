#Kuttys Playground

class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

class TreeInfo:
    def __init__(self):
        self._visited = False
        self._successor = None
    
    def updateVisited(self,result):
        self._visited = result
    
    def getVisited(self):
        return self._visited
    
    def updateSuccessor(self, successor):
        self._successor = successor
    
    def getSuccessor(self):
        return self._successor

def inOrderTraverse(tree, treeInfo:TreeInfo,node):
    if tree is None or treeInfo.getSuccessor() is not None :
        return

    inOrderTraverse(tree.left, treeInfo,node)
	
    if treeInfo.getVisited():
        treeInfo.updateSuccessor(tree)
        treeInfo.updateVisited(False)

    if tree.value == node.value:
        treeInfo.updateVisited(True)

    inOrderTraverse(tree.right, treeInfo,node)

		
def findSuccessor(tree, node):
    # Write your code here.
    treeInfo = TreeInfo()
    inOrderTraverse(tree, treeInfo,node)
    return treeInfo.getSuccessor()
