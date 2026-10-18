# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        out = []
        level = deque()
        level.append(root)
        while level:
            for i in range(len(level)):
                add = level.popleft()
                if add.left:
                    level.append(add.left)
                if add.right:
                    level.append(add.right)
            out.append(add.val)

        return out