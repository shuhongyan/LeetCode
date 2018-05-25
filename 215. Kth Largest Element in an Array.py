#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 05:22:14 2018

@author: shuhongyan
"""
#40ms
#第一种方法很容易思考，用sort()就好
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #第k大的就是sorted之后的倒数第k个
        nums.sort()
        return nums[-k]
    
#760ms
#然后思考了一下不用sort的方法，就是找到一个最大值，把这个最大值从list里remove掉
#remove掉k－1次的时候，下一个最大值就是第k个最大值了，但是这样如果K很大的话，耗时就会很长
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #不通过sort()的话
        while k>0:
            m = max(nums)
            nums.remove(m)
            k-=1
        return m
#268ms
#改进一下上面的方法如果k小于list长度的一半，还是找第k个最大值
#如果k大于list长度的一半，那就直接找相应的最小值而不是最大值
#这样while loop运行次数控制在了len(nums)/2次以内
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        if k<len(nums)/2:
            while k>0:
                m = max(nums)
                nums.remove(m)
                k-=1
            return m
        else:
            i = len(nums)-k+1
            while i>0:
                m = min(nums)
                nums.remove(m)
                i-=1
            return m
#我看论坛里还有整random index开始弄的，没仔细看，但是这样runtime就得看运气了，之后复习的时候可以再瞅瞅