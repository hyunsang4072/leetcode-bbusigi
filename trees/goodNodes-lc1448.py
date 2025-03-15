# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(self, root: TreeNode) -> int:
    # keep track of maximum value for each path
    # traverse each node using dfs
    # TC: O(n)
    # SC: O(n)
    res = 0

    # no return value for dfs since
    # we use the global variable "res"
    def dfs(t, curr):
        nonlocal res
        if not t: return

        # can be the same as current max value
        if t.val >= curr:
            res += 1
        
        # update current max value along the path
        curr = max(curr, t.val)
        
        dfs(t.left, curr)
        dfs(t.right, curr)
    
    # call dfs on the root node
    dfs(root, root.val)

    return res