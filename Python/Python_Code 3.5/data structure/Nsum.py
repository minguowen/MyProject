# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 13:44:55 2016

@author: Stranger
"""

class Solution():
    def twoSum(self,nums,target):
        '''无重复数字
        '''
        nums.sort()
        L = len(nums)
        left = 0
        right = L-1
        res = []
        while left < right:
            temp = nums[left]+nums[right]
            if temp == target:
                res.append([nums[left],nums[right]])
                right-=1
                left+=1
            elif temp>target:
                right-=1
            else:
                left+=1
        return res
        
    def threeSum(self,nums,target):
        
        
        
        
        
if __name__ == '__main__':
    a = Solution()
    nums = [0,3,7,9,11,13,16,17]
    target = 20
    res = a.twoSum(nums,target)
            
    n = range(1,5+1)    
        
        