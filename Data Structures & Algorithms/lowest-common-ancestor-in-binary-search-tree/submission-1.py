# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if(p.val<q.val):
            while root.val<p.val:
                root = root.right
            while root.val>q.val:
                root = root.left
            while root.val<p.val:
                root = root.right
            return root
        else:
            while root.val<q.val:
                root = root.right
            while root.val>p.val:
                root = root.left
            while root.val<q.val:
                root = root.right
            return root
            