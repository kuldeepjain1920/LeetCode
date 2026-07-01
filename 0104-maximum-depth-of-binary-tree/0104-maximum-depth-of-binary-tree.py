# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

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

        ## BFS
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
