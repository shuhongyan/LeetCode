#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 23:04:58 2018

@author: shuhongyan
"""
#没啥好说的，判断nums1里的每个元素在不在nums2里面，如果在nums2里面而且不在返回的lst里，就加进去
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lst = []
        for i in nums1:
            if i in nums2 and i not in lst:
                lst.append(i)
        return lst
            