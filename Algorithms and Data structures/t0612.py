class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def height(self, root):
        if root:
            if root.left:
                return 1 + self.height(root.left)
            if root.right:
                return 1 + self.height(root.right)
            return 0
        return 1
            