# Kutty's playground.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    #inorder gives tree in sorted form
    ele = inOrder(tree,[])
    k%=len(ele)
    return ele[-k] if k<len(ele) else -1

def inOrder(root,array):
    if not root:
        return array
    array.append(root.value)
    inOrder(root.left,array)
    inOrder(root.right,array)
    return array