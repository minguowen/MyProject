# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 23:35:49 2016

@author: Stranger
"""

class Solution():
    def MaxSunarray(self,nums):
        L = len(nums)
        subMax = nums[0]
        res = subMax
        fro = 0
        to = 0
        for i in range(1,L):
            subMax = max(subMax+nums[i],nums[i])
            if subMax == nums[i]:
                fro = i
            if subMax>res:
                to = i
            res = max(res,subMax)
            
        return res,nums[fro:to+1]
    
if __name__ == '__main__':
    nums = [1,-2,3,10,-4,7,2,-5]
    a = Solution()
    res = a.MaxSunarray(nums)