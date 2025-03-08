# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    res = 0

    # returns the height, not diameter!!!
    def dfs(t: Optional[TreeNode]) -> int:
        # this makes our res points to the global variable res defined outside this function
        nonlocal res # not a local varaible

        if not t:
            return 0
        
        left = dfs(t.left)
        right = dfs(t.right)
        d = left + right # actual diameter of current tree

        res = max(res, d) # update res

        # we don't return res here
        # because we want to return the height of current tree + 1
        return 1 + max(left, right)
    
    dfs(root) # update res

    return res