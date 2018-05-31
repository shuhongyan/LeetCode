#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 23:50:01 2018

@author: shuhongyan
"""
#前看数字里有没有0，没有的话就一个个字符看能不能整除这个数字。
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def f(i,lst):
            t = i
            while t>0 :
                if i % (t%10) !=0:
                    return
                t = int(t/10)
            return i
        lst = []
        status = True
        for i in range(left,right+1):
            if '0' not in str(i) and i == f(i,lst):
                lst.append(i)

        return lst