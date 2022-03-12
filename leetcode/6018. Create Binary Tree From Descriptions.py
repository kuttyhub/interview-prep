class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createBinaryTree( descriptions):
    hashMap ={}
    root = None
    for val,child,direction in descriptions:
        if hashMap.get(val) is None:
            hashMap[val] = TreeNode(val)
            root = hashMap[val]
        if direction == 0:
            if hashMap.get(child) is None:
                hashMap[val].right=TreeNode(child)
            else:
                hashMap[val].right=hashMap[child]
        elif direction == 1:
            if hashMap.get(child) is None:
                hashMap[val].left=TreeNode(child)
            else:
                hashMap[val].left=hashMap[child]
    # print(hashMap)

descriptions = [[1,2,1],[2,3,0],[3,4,1]]
createBinaryTree(descriptions)
