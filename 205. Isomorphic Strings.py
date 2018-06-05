# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 10:54:58 2018

@author: yans1
"""
#建个空dic， s相应的位置对应t的value
#如果s里的值不在dic里，就判断对应的t值有没有被用过，如果没有被用过就能让s值对应t值；如果用过了就不是相似的了
#如果s值在dic里，就判断s值是否等于dic里s对应的t值，等于就继续，不等于就return False
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for i, j in zip(s,t):
            if i not in dic:

                if j in dic.values():
                    return False
                dic[i]= j
            elif dic[i]!=j:
                return False
        return True