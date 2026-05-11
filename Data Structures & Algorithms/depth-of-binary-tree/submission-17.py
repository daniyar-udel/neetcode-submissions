# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        max_depth = 0

        stack = list()

        stack.append((root, 1))


        while stack:
            node, depth = stack.pop()
            if node:
                stack.append((node.right, depth + 1))
                stack.append((node.left, depth + 1))
                max_depth = max(max_depth, depth)
        
        return max_depth
