class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
def height(root):
    if not root:
        return 0
    return 1+max(height(root.left),height(root.right))

#example usage
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
print(height(root))