#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 06:27:29 2018

@author: shuhongyan
速度所有都是36ms
"""
#这是我最开始自己写的，然后循环让A的前面1，2。。个数字都放到最后去看等不等于B
class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A==B:#保证AB都是空list“”的时候还能返回True
            return True
        if sorted(A)==sorted(B):
            i=0
            while i<len(A):
                if A[i:]+A[:i]==B:
                    return True
                i+=1
            return False
        else:
            return False
#然后发现不需要用sorted()这么复杂的语句，在判断A变形后是否等于B的时候就包含了sorted()的功能
#所以去掉了一个if语句，再把while loop换成for loop
class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A==B:
            return True          
        for i in range(len(A)):
            if A[i:]+A[:i]==B:
                return True           

        return False
#这个是看了别人的分析后，又可以省掉一个开头if来判断当AB都是空集情况的语句     
#空集l： l[0]是语法错误，但是l[:0]or l[0:]都是返回空集""的
#for循环的长度变成len(A)+1保证了for loop在空集情况下还能执行一次，从而省略前面方法里用到的if语句
 class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        for i in range(0, len(A)+1):
            if A[i:] + A[:i] == B:
                return True
        return False
#这个超牛的，别人的one line code，哈哈哈       
class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)==len(B) and A in B+B:
            return True
        else:
            return False
        
        