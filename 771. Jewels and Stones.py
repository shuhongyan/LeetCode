# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 10:39:43 2018

@author: yans1
"""
#思路就是统计J里每个字母在S里出现的次数。list.count()了解一下
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        s = 0
        for j in J:
            s += S.count(j)
        return s