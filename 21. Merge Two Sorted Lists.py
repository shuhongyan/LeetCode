#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 04:38:30 2018

@author: shuhongyan
"""
#56ms
#还没学到这一部分，但是感觉跟二叉树差不多的逻辑
#建l空集，用recursive 比较l1，l2当前value大小，小的排进l，然后那个list指针指向next，继续比较当前俩list值的大小
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = ListNode(None)
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            l.val = l1.val
            l.next = self.mergeTwoLists(l1.next,l2)
        if l1.val >l2.val:
            l.val = l2.val
            l.next = self.mergeTwoLists(l1,l2.next)
        return ls