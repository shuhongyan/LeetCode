# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 16:41:53 2018

@author: yans1
"""

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers)-1
        while i<j:
            if i>0 and numbers[i] ==numbers[i-1]:
                i+=1
                continue
            if j<len(numbers)-1 and numbers[j]==numbers[j+1]:
                j-=1
                continue
            s = numbers[i]+numbers[j]
            if s == target:
                return [i+1,j+1]
            elif s<target:
                i +=1
            else:
                j -=1
        return []
            