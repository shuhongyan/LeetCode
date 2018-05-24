#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 20:07:30 2018

@author: shuhongyan
"""
#因为是按顺序排列的，所以从i=0开始，nums[i]==nums[i+1]，如果不等于，nums[i]就是那个只出现过一次的数
#唯一的特例是那个只出现过一次的数是数列最后一位，所以while loop函数只要判断到数列的倒数第三位
#如果还没找到，就必然是最后一个是单着的，直接return就行

class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        if nums ==[]:
            return None #首先先判断是否为空集
        while i<len(nums)-2: #然后用while loop 判断到倒数第三个数
            if nums[i]!=nums[i+1]:
                return nums[i]
            i +=2
        return nums[i]#前面的都找不到就return最后一个元素