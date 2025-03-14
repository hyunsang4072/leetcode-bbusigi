# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # Iterative approach
    # TC: O(h), where h = height(root)
    # SC: O(1)
    curr = root

    while curr:
        if curr.val < p.val and curr.val < q.val:
            curr = curr.right
        elif curr.val > p.val and curr.val > q.val:
            curr = curr.left
        else:
            return curr

    ####### Recursive approach #######
    # TC: O(h), where h = height(root)
    # SC: O(h)
    # if not root.left or not root.right:
    #     return root
    
    # if root.val == p.val: return p
    # if root.val == q.val: return q

    # if root.val < p.val and root.val < q.val:
    #     return self.lowestCommonAncestor(root.right, p, q)
    # elif root.val > p.val and root.val > q.val:
    #     return self.lowestCommonAncestor(root.left, p, q)
    # else:
    #     return root