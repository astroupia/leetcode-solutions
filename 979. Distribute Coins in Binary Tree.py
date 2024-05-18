# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        
        def value(root):
            if root is None:
                return 0
            left_excess = value(root.left)
            right_excess = value(root.right)
            
            self.moves += abs(left_excess) + abs(right_excess)
            return root.val - 1 + left_excess + right_excess
        
        value(root)
        return self.moves