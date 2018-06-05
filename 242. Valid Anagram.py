# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 14:24:59 2018

@author: yans1
"""
#这个很简单，就是用sorted 排序s，t。如果排序后两者一样就return True，否则他return False
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s)==sorted(t)