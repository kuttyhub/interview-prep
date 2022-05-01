#kuttt's Plaground

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Helper:
    def __init__(self):
        self._isBalanced = True

    def updateBalanced(self,result):
        self._isBalanced = result

    def getBalanced(self):
        return self._isBalanced

def getHeight(tree, helper):
    if tree is None :
        return 0

    leftHeight = getHeight(tree.left, helper)
    rightHeight = getHeight(tree.right, helper)
	
    differnce= abs(leftHeight - rightHeight)
	
    if differnce>1 and helper.getBalanced():
        helper.updateBalanced(False)
    
    return max(leftHeight,rightHeight)+1 


def heightBalancedBinaryTree(tree):

    helper = Helper()
    getHeight(tree, helper)
    return helper.getBalanced()
