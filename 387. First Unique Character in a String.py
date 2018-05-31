# -*- coding: utf-8 -*-
"""
Created on Thu May 31 16:43:59 2018

@author: yans1
"""

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #这么短的代码runtime竟然辣么长！生气
        i=0
        
        while i<len(s):
            if s[i+1:].find(s[i]) == -1 and s[i] not in s[:i]:
                return i
            i += 1
        return -1