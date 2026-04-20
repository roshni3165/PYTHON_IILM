from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res, q, rev = [], deque([root]), False
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            res.append(level[::-1] if rev else level)
            rev = not rev
        
        return res