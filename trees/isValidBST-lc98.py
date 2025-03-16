# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(self, root: Optional[TreeNode]) -> bool:
    # optimal approach
    # TC: O(n)
    # SC: O(n)
    def dfs(t, left, right):
        # t = node
        # left, right = value, value
        if not t: return True

        if not (left < t.val < right):
            return False

        # look at the test cases to figure out why this works...
        # [5,4,6,null,null,3,7]
        return dfs(t.left, left, t.val) and dfs(t.right, t.val, right)
    
    return dfs(root, float("-inf"), float("inf"))

    # my approach using global variables with in-order traversal
    # res = float("-inf")
    # isValid = True
    # def dfs(t):
    #     nonlocal res
    #     nonlocal isValid

    #     if not t: return

    #     # left recurse first
    #     dfs(t.left)

    #     # in-order
    #     if res >= t.val:
    #         isValid = False
        
    #     res = t.val

    #     # right recurse
    #     dfs(t.right)
    
    # dfs(root)
    
    # return isValid