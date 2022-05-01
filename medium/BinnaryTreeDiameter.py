class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, depth =0):
        self._depth = depth
    
    def updateDepth(self, depth):
        self._depth = depth
		
    def getDepth(self):
        return self._depth

def getHeight(tree,treeInfo):
    # Write your code here.
    if tree is None:
        return 0
    
    leftHeight = getHeight(tree.left,treeInfo)
    rightHeight = getHeight(tree.right,treeInfo)
    newHeight = max(leftHeight+rightHeight,treeInfo.getDepth())
    treeInfo.updateDepth(newHeight)

    return max(leftHeight,rightHeight)+1

def binaryTreeDiameter(tree):
    # Write your code here.
    treeInfo =TreeInfo()
    getHeight(tree,treeInfo)
    return treeInfo.getDepth()