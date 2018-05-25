#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 22:24:41 2018

@author: shuhongyan
"""

class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        s=""
        if t is None:
            return ""
        def f(t,s):
            s += str(t.val)

            if t.left or t.right:
                s +="("
                if t.left:
                    s=f(t.left,s)
                s += ')'
                if t.right:
                    s +="("
                    s=f(t.right,s)
                    s += ')'
            return s
        return f(t,s)
#看完解析后照着那个思路自己又写了一遍。确实是比自己之前想的简单
#下面这个方法好像在你之前的inorder binary tree就见过
#当时没咋懂，现在懂了
class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """

        if t is None:
            return ""
        if t.left is None and t.right is None:
            return str(t.val)+""
        if t.right is None:
            return str(t.val)+"("+self.tree2str(t.left)+")"
        else:
            return str(t.val) +"("+self.tree2str(t.left)+")"+"("+self.tree2str(t.right)+")"
        

        