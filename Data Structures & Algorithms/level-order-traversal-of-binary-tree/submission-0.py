# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        def dfs(root, level):
            if not root:
                return None
            if level > len(self.res) - 1:
                self.res.append([])
            self.res[level].append(root.val)
            left = dfs(root.left, level + 1)
            right = dfs(root.right, level + 1)
        
        dfs(root, 0)
        return self.res


            