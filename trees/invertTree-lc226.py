# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # pretty basic DFS problem
    if not root:
        return None
    
    # we can just swap left and right child nodes RECURSIVELY
    root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

    return root