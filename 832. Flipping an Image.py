#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 22:56:14 2018

@author: shuhongyan
"""
#先reverse 在invert嘛
#reverse就是循环一半就好了，第一个跟倒数第一个互换；第二个跟倒数第二个互换。。。
#invert就是每个循环等于1换成0，等于0换成1
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        def reverse(lst):
            mid = int(len(lst)/2)
            for i in range(mid):  
                lst[i],lst[-(i+1)] = lst[-(i+1)],lst[i]
            
            for i in range(len(lst)):
                if lst[i] == 0:
                    lst[i] = 1
                else:
                    lst[i] = 0
            return lst
        for lst in A:
            lst = reverse(lst)
            
        return A

                    


                    
