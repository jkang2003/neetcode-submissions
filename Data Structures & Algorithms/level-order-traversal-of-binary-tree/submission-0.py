# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        out = []
        deck = deque()
        deck.append(root)
        while deck:
            level = []
            for i in range(len(deck)):
                node = deck.popleft()
                if node:
                    level.append(node.val)
                if node.left:
                    deck.append(node.left)
                if node.right:
                    deck.append(node.right)
            out.append(level)
        return out
            