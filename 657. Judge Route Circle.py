# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 13:58:26 2018

@author: yans1
"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        #左走步数等于右走步数；向上步数等于向下步数
        #nums(U)=nums(D) and nums(L)=nums(R)
        
        if len(moves)%2 !=0:
            return False
        def f(moves,letter):
            length = len(moves)
            moves = moves.replace(letter,'')
            return (length - len(moves)),moves

        DL, moves = f(moves, 'D')
        UL, moves = f(moves, 'U')
        if DL !=UL:
            print (DL,UL)
            return False
            
        LL, moves = f(moves, 'L')
        RL, moves = f(moves, 'R')
        print(LL,RL)
        if LL==RL:
            return True
        return False
        
#后来才发祥有专门算count的语法 用list.count(),一句代码搞定
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        #左走步数等于右走步数；向上步数等于向下步数
        #nums(U)=nums(D) and nums(L)=nums(R)
        
        return moves.count('D') == moves.count('U') and moves.count('L') == moves.count('R')
