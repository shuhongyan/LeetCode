# -*- coding: utf-8 -*-
"""
Created on Wed May 16 12:45:56 2018

@author: yans1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#基本逻辑就是判断root.val==0以及左边的树root.left and root.right都是0
#从底下往上砍，尾巴都是0，就一路往上砍，不是就保留。
class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root == None:
            return None
        root.left=self.pruneTree(root.left)
        root.right=self.pruneTree(root.right)
        if root.val == 0 and root.left == None and root.right == None:
            root =None
        return root