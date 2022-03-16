# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    ele = postOrder(tree,[])
    ele.sort()
    k%=len(ele)

    return ele[-k] if k<len(ele) else -1

def postOrder(root,array):
    if not root:
        return array
    postOrder(root.left,array)
    postOrder(root.right,array)
    array.append(root.value)
    return array