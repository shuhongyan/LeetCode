# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 15:56:09 2018

@author: yans1
"""

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        lst = []
        nums.sort()
        if len(nums)<4 :
            return []
        l = len(nums)
        for i in range(l-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, l-2):
                if j==i+1 or nums[j]!=nums[j-1]:                    
                    left = j+1
                    right = l-1
                    while left<right:
                        s = nums[i] + nums[j] + nums[left] + nums[right]
                        if s == target:
                            sub_lst = [nums[i],nums[j],nums[left],nums[right]]
                            if sub_lst not in lst:
                                lst.append(sub_lst)
                            left += 1
                            right -=1
                        elif s<target:
                            left += 1
                        else:
                            right -=1
        return lst