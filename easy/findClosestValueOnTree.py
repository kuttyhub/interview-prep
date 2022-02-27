class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree, target,ele=0,minDiff=float("inf")):
    if tree is None:
        return ele
        
    dif = abs(target-tree.value)
    if minDiff>dif:
        minDiff = dif
        ele = tree.value
        
    if tree.value <target:
        return findClosestValueInBst(tree.right,target,ele,minDiff)
    else:		 
        return findClosestValueInBst(tree.left,target,ele,minDiff)
