# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def dfs(root):
        if not root:
            return 0
        
        left = dfs(root.left)
        right = dfs(root.right)

        # if unbalanced tree, return -1
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        
        # in normal(balanced) case, return height of current tree
        return 1 + max(left, right)

    # if return -1, somewhere in tree not balanced portion
    return dfs(root) != -1