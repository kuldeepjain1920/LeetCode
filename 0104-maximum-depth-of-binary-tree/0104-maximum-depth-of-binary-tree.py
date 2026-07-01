# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        ## DFS recursion
        ## Time: O(n) — every node visited once. 
        ## Space: O(h) — recursion stack, h = tree height (worst case O(n) for a skewed tree).
        ## 
        if not root: return 0
        return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))
        