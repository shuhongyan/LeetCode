# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:31:19 2018

@author: yans1
"""
#做了好久才知道binary search tree的定义。。。还在思考先判断做还是先判断右。。。
#不过递归的逻辑我到现在还是一知半解的，感觉木有理解透彻啊。。得多刷点题
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        
        
        tree = TreeNode(None)
        if root == None:
            return None
        if root.val > R:
            return self.trimBST(root.left,L,R) #开始这还有下面抖没有弄return，看了你的以后思考半天才想明白
        if root.val < L:
            return self.trimBST(root.right,L,R) 
        else:
            tree.val = root.val #感觉你的比我的精简些，直接改root就不用新建一个空tree了
        tree.left = self.trimBST(root.left,L,R) 
        tree.right = self.trimBST(root.right,L,R)

        return tree
        