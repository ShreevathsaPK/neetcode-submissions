# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        que = deque([p])
        que2 = deque([q])
        while que:
            root = que.pop()
            root2 = que2.pop()
            if not root and not root2:
                continue
            if root and not root2:
                return False
            if root2 and not root:
                return False
            if root.val!=root2.val:
                return False
            que.append(root.left)
            que.append(root.right)
            que2.append(root2.left)
            que2.append(root2.right)
        return True



