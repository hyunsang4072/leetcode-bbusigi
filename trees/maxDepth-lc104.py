# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth(self, root: Optional[TreeNode]) -> int:
    # RECURSIVE dfs approach
    # TC: O(n)
    # SC: O(h), where h = height(tree)
    if not root:
        return 0

    return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))