# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 23:39:58 2016

@author: Stranger
"""

class Solution():
    def twoDiff(self,nums,diff):
        L = len(nums)
        if L == 0 or L == 1:
            return None
        res = []
        left = 0
        right = 1
        nums.sort()
        while right<L:
            temp = nums[right]-nums[left]
            if temp == diff:
                res.append([nums[left],nums[right]])
                left+=1
                right+=1
            elif temp<diff:
                right+=1
            else:
                left+=1
        return res
            
if __name__=='__main__':
    a = Solution()
    nums = [0,3,7,9,11,14,16,17]
    res= a.twoDiff(nums,7)
        
        