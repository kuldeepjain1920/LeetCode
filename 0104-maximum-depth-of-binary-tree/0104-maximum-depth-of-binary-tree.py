# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        """
        "For a balanced tree, DFS uses O(log n) stack space versus BFS 
        using O(n) queue space at the widest level — DFS wins. For a skewed 
        tree, DFS uses O(n) stack space and risks a stack overflow, while BFS 
        uses O(1) queue space since each level has one node — BFS wins. 
        The right choice depends on the expected shape of the input tree.
        All 4 approaches
        #Approach           Time    Space   Key data structure
        1. DFS Recursive    O(n)    O(h)    Call stack (implicit)
        2. BFS Iterative    O(n)    O(w)    Queue (deque)
        3. DFS Iterative    O(n)    O(h)    Stack (explicit)
        4. Morris Traversal O(n)    O(1)    No extra space at all

        ---------------------------------------------------------------------------------------------
        Approach            When to use
        ---------------------------------------------------------------------------------------------
        DFS Recursive       Always lead with this — clearest, most concise
        BFS Iterative       Offer when interviewer asks about skewed trees or stack overflow
        DFS Iterative       Mention as "same as DFS recursive but avoids Python's recursion limit"
        Morris Traversal    Only if interviewer explicitly asks for O(1) space — very rare
        """

        """
        ## DFS recursion
        ## Time: O(n) — every node visited once.
        ## Space: O(h) — recursion stack, h = tree height (worst case O(n) for a skewed tree).
        ## Runtime 0ms beats 100%
        ## Memory 20.25 Beats 61.41
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        """

        ## DFS iterative
        ## Time O(n) Space O(h) Stack (explicit)
        ## Avoids Python's recursion limit
        ## Run time O ms Beats 100%
        ## Memory 20.37 MB Beats 24.54% 
        
        if not root: return 0

        stack = [(root, 1)] ## node, depth at this node
        max_d = 0
        while stack:
            node, d = stack.pop() #LIFO depth first
            max_d = max(max_d, d)

            if node.left: stack.append((node.left, d+1))
            if node.right: stack.append((node.right, d+1))
        return max_d

        """
        ## BFS Iterative
        ## O(n) time, O(w) space w = width of the Tree; bottom row w=n/2
        ## Runtime 0 ms Beats 100%
        ## Memory 20.45 MB Beats 5.10% 
        if not root: return 0
        queue, depth = deque([root]), 0

        while queue:
            depth += 1

            for _ in range(len(queue)): ## number of nodes in current level i.e. BFS
                node = queue.popleft() ## remove from front;
                ## within each level, process nodes left to right.
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
        return depth
        """

if __name__ == "__main__":
    sol = Solution()

    def buildTrees(values):
        if values is None or values[0] is None:
            return None

        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop()

            if i < len(values):
                node.left = TreeNode(values[i])
                queue.append(node.left)
                i += 1
            if i < len(values):
                node.right = TreeNode(values[i])
                queue.append(node.right)
                i += 1
        return root

    def test_empty_tree():
        assert sol.maxDepth(None) == 0

    def test_single_node():
        root = buildTrees([5])
        assert sol.maxDepth(root) == 1

    test_empty_tree()
    test_single_node()
