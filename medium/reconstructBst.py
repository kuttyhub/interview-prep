#kutty's playground

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self,rootIdx) :
        self.rootIdx= rootIdx

def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return helper(preOrderTraversalValues,float("-inf"),float("inf"),treeInfo)

def helper(array,leftBound,rightBound,treeInfo):
    if len(array) == treeInfo.rootIdx:
        return None

    currentValue = array[treeInfo.rootIdx]

    if currentValue< leftBound or currentValue>=rightBound:
        return None

    treeInfo.rootIdx +=1

    leftTree = helper(array,leftBound,currentValue,treeInfo)
    rightTree = helper(array,currentValue,rightBound,treeInfo)

    return BST(currentValue,leftTree,rightTree)

