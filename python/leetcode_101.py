from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def bfs(root: TreeNode, direction: bool):
            q = deque([root])
            history = [root]
            while q:
                v = q.popleft()

                if direction:
                    history.append(v.left)
                    history.append(v.right)

                    if v.left:
                        q.append(v.left)
                    if v.right:
                        q.append(v.right)
                else:

                    history.append(v.right)
                    history.append(v.left)

                    if v.right:
                        q.append(v.right)
                    if v.left:
                        q.append(v.left)

            return [v.val if v else None for v in history]

        A = bfs(root, True)
        B = bfs(root, False)
        for i, a in enumerate(A):
            if a != B[i]:
                return False

        return True


# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         def ismirror(t1, t2):
#             if t1 is None and t2 is None:
#                 return True

#             if t1 is None or t2 is None:
#                 return False

#             return t1.val == t2.val and ismirror(t1.right, t2.left) and ismirror(t1.left, t2.right)

#         return ismirror(root, root)
