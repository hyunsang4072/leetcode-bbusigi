# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # 3 base cases
    if not root: # base case 1: if no root, there's no way for the subRoot to be a subTree of root
        return False
    
    if not subRoot: # base case 2: if no subRoot, it will always be a subtree of root
        return True
    
    if self.isSameTree(root, subRoot): # base case 3: if same tree, it satisfies the subtree definition
        return True

    # check left and right of the root using DFS
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

def isSameTree(self, r, t):
    if not r and not t:
        return True
    
    if r and t and r.val == t.val:
        return self.isSameTree(r.left, t.left) and self.isSameTree(r.right, t.right)
    else:
        return False