# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 14:15:11 2018

@author: yans1
"""
#跟205 Isomorphic Strings类似逻辑。但是要把str用split（）分解成一个list
#然后多考虑list的长度要等于pattern的长度
#以及dic.get(key)了解一下
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        lst = str.split()
        dic = {}
        if len(lst) != len(pattern):
            return False
        for i, j in zip(pattern, lst):
            if i not in dic:
                if j in dic.values():
                    return False
                dic[i] = j
            elif dic[i] != j:
                return False
        return True