
# inorder, dfs
# 문제를 제대로 이해하지 못했었다.
# 릿코드의 문제 제출방법에 대해서 숙지하지 못했다.
# 받은 root의 값 자체를 변화시키고 root를 다시 리턴한다.
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.right)
            self.sum += node.val
            node.val = self.sum
            inorder(node.left)
            
        inorder(root)
        return root