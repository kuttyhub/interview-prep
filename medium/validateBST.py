#kutty's Playground

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validityOfBST(tree,float("-inf"),float("inf"))

def validityOfBST(node,min,max):
    if not node:
        return True
    if node.value <min or node.value>max:
        return False
    return validityOfBST(node.left,min,node.value-1) and validityOfBST(node.right,node.value,max)