# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 11:17:25 2016

@author: Stranger
"""

class Solution():
    def MaxSequence(self,nums):
        L = len(nums)
        if L == 0:
            return 0
        mx = 1
        temp = 1
        left = 0
        right = 1
        res = []
        while right < L:
            if nums[right]-nums[right-1] == 1:
                temp+=1
                right+=1
            else:
                if temp>mx:
                    mx = temp
                    res = nums[left:right]
                temp = 1
                left = right
                right+=1
        return mx,res
        
        
if __name__ == '__main__':
    a = Solution()
    nums = [1,2,3,4,5,6,7,5,6,56,57,58,59,60,55]
    res = a.MaxSequence(nums)
        
                
            
            
        