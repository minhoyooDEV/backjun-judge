# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        d = defaultdict(int)

        def dfs(root: TreeNode):

            if root:
                d[root.val] += 1

                dfs(root.left)
                dfs(root.right)

        dfs(root)
        mx = 0
        for key in d:
            mx = max(d[key], mx)

        ans = []
        for key in d:
            if d[key] == mx:
                ans.append(key)

        return ans


class Solution2:
    def findMode(self, root: TreeNode) -> List[int]:
        prev_val = max_cnt = curr_cnt = float('-inf')
        modes = []

        left_branch = []
        while root:
            left_branch.append(root)
            root = root.left

        while left_branch:
            curr_node = left_branch.pop()
            curr_val, right = curr_node.val, curr_node.right

            if curr_val != prev_val:
                curr_cnt = 1
            else:
                curr_cnt += 1
            prev_val = curr_val

            if max_cnt == curr_cnt:
                modes.append(curr_val)
            elif max_cnt < curr_cnt:
                modes = [curr_val]
                max_cnt = curr_cnt

            while right:
                left_branch.append(right)
                right = right.left

        return modes
