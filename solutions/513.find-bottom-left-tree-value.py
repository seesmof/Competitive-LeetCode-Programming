#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def findBottomLeftValue(self, root: TreeNode) -> int:
#         q = deque([root])
#         while q:
#             node = q.popleft()
#             if node.right:
#                 q.append(node.right)
#             if node.left:
#                 q.append(node.left)
#         return node.val

# @lc code=end
