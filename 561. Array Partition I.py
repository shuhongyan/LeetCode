# -*- coding: utf-8 -*-
"""
Created on Sat May 19 16:15:14 2018

@author: YANS1
"""
#思路就是按照从小到大排列，按顺序两两组合取出的每个list里最小值求和就是最大的
#所以首先应该把nums里所有元素顺序按照重大到小重新排列
#然后取1,3,5,7....len(nums)-1位的元素总和

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()#让list里的元素按从小到大重新排列
        s = 0 
        i = 0
        while i<len(nums):
            s += nums[i] #把位置处于单位数的元素相加求和
            i += 2
            
        return s