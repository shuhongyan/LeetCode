#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 20:43:29 2018

@author: shuhongyan
"""
#原理就是t1没有就return t2; t1.left没有，就return t2.left; t1.left没有就return t2.left
#反之也是
#类似于preorder 二叉树，如果二者都有，新树就是二者树的数值之和，然后再判断left and right
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        t = TreeNode(None)
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t.val = t1.val+t2.val
        if t1.left or t2.left:
            t.left = TreeNode(None)
            t.left = self.mergeTrees(t1.left,t2.left)
        if t1.right or t2.right:
            t.right = TreeNode(None)
            t.right = self.mergeTrees(t1.right,t2.right)

        return t
#看了你的代码后发现自己是写重复了。。。原理是一样的，没必要像我先前那样if再来一下，迭代方程里有
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        t = TreeNode(None)
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        t.val = t1.val+t2.val
        t.left = self.mergeTrees(t1.left,t2.left)
        t.right = self.mergeTrees(t1.right,t2.right)

        return t