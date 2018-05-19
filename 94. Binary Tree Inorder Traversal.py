# -*- coding: utf-8 -*-
"""
Created on Sat May 19 16:22:32 2018

@author: YANS1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        def f(root,lst):
            if root.left:
                f(root.left,lst)
            lst.append(root.val)
            if root.right:
                f(root.right,lst)
            return lst
        lst = []
        return f(root,lst)
        