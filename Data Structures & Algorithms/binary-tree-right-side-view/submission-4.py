# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        out = []
        q = deque()
        q.append(root)
        
        while q:
            rightSide = None
            for i in range(len(q)):
                rightSide = q.popleft()
                if rightSide.left: q.append(rightSide.left)
                if rightSide.right: q.append(rightSide.right)

            if rightSide: out.append(rightSide.val)
        return out