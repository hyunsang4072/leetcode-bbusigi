# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(self, root: Optional[TreeNode]) -> int:
    res = [root.val] # this is to avoid having to deal with global v. local variables

    def dfs(t):
        if not t: return 0

        leftMax = dfs(t.left) # recurse left
        rightMax = dfs(t.right) # recurse right
        
        # we don't want to take in a value if it's negative
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        # update current maxPathSum so far
        # this is when we don't want to split when recursing down
        # either right or left subtrees
        res[0] = max(res[0], t.val + leftMax + rightMax)

        # this is when we want to split(think "taking a turn" while recursing)
        return t.val + max(leftMax, rightMax)
    
    dfs(root)

    return res[0]