# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 14:22:45 2018

@author: yans1
"""
#要求abs(target - sum)的最小值
#固定一个数，然后采用二分法。固定的数从nums[0]开始往后变，left就是固定数右边那个数，right就是nums[-1]
#比较最小差值
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        result = nums[-3]+nums[-2]+nums[-1]
        diff = abs(result - target)
        for i in range(len(nums)-2):
            if i>0 and nums[i] ==nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1

            while l<r:

                s = nums[i]+nums[l]+nums[r]
                tdiff = abs(s-target)
                if tdiff<diff:
                    result = s
                    diff = tdiff
                if s<target:
                    l+=1
                elif s>target:
                    r-=1
                else:
                    return s

        return result
        