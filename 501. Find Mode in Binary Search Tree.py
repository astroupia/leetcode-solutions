# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        curr_node = root
        result = []
        curr_streak = 0
        curr_num = float("inf")
        max_streak = 0

        while curr_node:
            if curr_node.left:
                neighbor = curr_node.left
                while neighbor.right is not None:
                    neighbor = neighbor.right
                neighbor.right = curr_node
                
                tmp = curr_node.left
                curr_node.left = None
                curr_node = tmp
            else: 
                if curr_node.val == curr_num:
                    curr_streak += 1
                else:
                    curr_streak = 0
                    curr_num = curr_node.val
                
                if curr_streak == max_streak:
                    result.append(curr_num)
                elif curr_streak > max_streak:
                    max_streak = curr_streak
                    result = [curr_num]
        
                curr_node = curr_node.right
        
        return result