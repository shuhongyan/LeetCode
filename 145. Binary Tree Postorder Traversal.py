# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#跟inorder binary tree逻辑是一样的。。弄懂postorder binary tree 的定义就很简单了
#先是left-->right-->root
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lst=[]
        def f(root,lst):
            if root is None:
                return None
            if root.left:
                f(root.left, lst)
            if root.right:
                f(root.right, lst)
            return lst.append(root.val) 

        f(root,lst)
        return lst
        