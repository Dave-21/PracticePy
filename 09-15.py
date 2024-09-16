# 09/15/2024

class Solution:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
        self.prev = None
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left is None and root.right is None:
            return True

        if not self.isValidBST(root.left):
            return False

        if self.prev is not None and root.val <= self.prev:
            return False

        self.prev = root.val

        return self.isValidBST(root.right)

        