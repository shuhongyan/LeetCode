# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 11:22:18 2018

@author: yans1
"""
#max(abs(i-j)*min(ai,aj))
#如果list特别大，这种一一审查的办法runtime就太长了
#所以这种方法不可取
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        water = 0

        for i, ele1 in enumerate(height):
            for j in range(i+1,len(height)):
                w = abs(i-j)*min(height[j],ele1)
                if w>water:
                    water = w
        return water
    #max(abs(i-j)*min(ai,aj))
    #所以采用二分法，从两头往中间靠。（i-j）会越来越小，ai，aj大小不定，需要比较
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        Hmax = 0
        Amax = 0
        i,j = 0, (len(height)-1)
        while i<j:
            if height[i]<height[j]:
                Htemp = height[i]
                i +=1

            else:
                Htemp = height[j]
                j -=1

            if Htemp>Hmax:
                Atemp = (j-i+1)*Htemp
                if Atemp>Amax:
                    Amax = Atemp
        return Amax