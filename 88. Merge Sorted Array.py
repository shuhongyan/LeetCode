#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 23:04:50 2018

@author: shuhongyan
"""
#runtime 40ms
#刚看懂binary search的逻辑就自个折腾自个，写了好几个小时才弄出来。。。再看懂都觉得是别人写的code，明明是原创 ＝_＝!
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        #因为nums1有足够的空间，所以肯定是把nums2里的元素插入nums1中。最后nums1的长度是m+n
        #来试试用binary search插入nums2里的每个元素
          
        if m!=0:
            l = 0
            r = m-1
            i = 0
            while i <len(nums2):
                while l<r:    
                    mid = int((l+r)/2)
                    if nums1[mid]<nums2[i]:
                        l = mid+1
                    elif nums1[mid]>nums2[i]:
                        r = mid-1
                    else:
                        l = mid
                        break
                if nums2[i]<nums1[l]:
                    nums1.insert(l,nums2[i])    
                else:
                    nums1.insert(l+1,nums2[i])
                    l = l+1
                r = m+i
                i +=1
                nums1.pop()
        else:
            nums1[:n]=nums2[:n]
            
#64ms
#另一种方法，语句短了很多，想法也容易多了，但是运行时间长了好多啊啊啊啊
#就是先把nums2一个一个插入nums2的最后面，然后sort一下就可以了
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while n+m<len(nums1):
            nums1.pop()
        while n>=1:
            nums1[m+n-1]=nums2[n-1]
            n -=1      
        nums1.sort()
            
            

        
            
            
        
        
            
            

        
            
            
        
        

        