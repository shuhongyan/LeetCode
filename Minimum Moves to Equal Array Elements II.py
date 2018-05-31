#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 22:48:01 2018

@author: shuhongyan
"""

class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #先找中位数;排序后找到中间位置的元素就是中位数
        if len(nums) == 1:
            return 0
        nums.sort()
        step = 0

        mid = int(len(nums)/2)
        for ele in nums:
            step += abs(nums[mid]-ele)
        return step