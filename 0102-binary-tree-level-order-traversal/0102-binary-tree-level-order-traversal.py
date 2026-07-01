# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        """
        Level-order traversal is inherently a BFS problem — BFS naturally processes 
        nodes level by level, which is exactly what we need. DFS solutions exist using 
        a depth index, but they're less intuitive and don't match the problem's structure.
        """

        ## BFS Iterative 
        ## Runtime 0 ms Beats 100%
        ## Memory 20.00 MB Beats 24.4%

        if not root: return []
        queue, depth = deque([root]), 0
        result = []

        while queue:
            level_size = len(queue)
            level_vals = []
            for _ in range(level_size):
                node = queue.popleft()
                level_vals.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            result.append(level_vals)
        return result

        """
        ## DFS Iterative
        ## Not a natural fit. NOT recommended for this problem

        if not root: return []
        result = []
        stack = [(root, 0)]     #(node, depth)

        while stack:
            node, depth = stack.pop()

            # First time visiting this depth — create a new level bucket
            if depth == len(result):
                result.append([])

            result[depth].append(node.val)
            
            # push right first so left is processed first (LIFO)
            if node.right: stack.append((node.right, depth+1))
            if node.left: stack.append((node.left, depth+1))

        return result
        """

        """
        ## DFS recursive
        ## Not a natural fit. NOT recommended for this problem
        result = [] 
        def dfs(node, depth):
            if not node: return

            # First time visiting this depth — create a new level bucket
            if depth == len(result):
                result.append([])

            result[depth].append(node.val)   # place value at correct level

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 0)
        return result
        """

        
