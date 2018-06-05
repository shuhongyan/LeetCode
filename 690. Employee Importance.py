#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 00:10:11 2018

@author: shuhongyan
"""

"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        #首先找到id的位置

        dic = {}
        for employee in employees:
            if employee.id == id:
                value = employee.importance
                sub_lst = employee.subordinates
            else:
                dic[employee.id] = [employee.importance, employee.subordinates]
                
        if not sub_lst:
            return value
        while sub_lst:
            sub_id = sub_lst.pop()
            value += dic[sub_id][0]
            if dic[sub_id][1]:
                sub_lst.extend(dic[sub_id][1])
        return value
                
            

 
