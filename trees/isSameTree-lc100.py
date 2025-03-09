# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # basically, the idea is that you traverse both trees simultaneously using dfs
    # TC: O(n)
    # SC: O(n) at worst; O(logn) at best
    if not p and not q:
        return True
    
    # check whether p and q not None
    # check their values if they are both not None
    if p and q and p.val == q.val:
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    else:
        return False