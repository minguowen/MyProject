# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 23:27:32 2016

@author: Stranger
"""

class Solution():
    def twoSearch(self,nums):
        L = len(nums)
        left = 0
        right = L-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]<nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return nums[right]


if __name__ == '__main__':
    a = Solution()
    nums = [1,2,3,1,4,5]
    res = a.twoSearch(nums)
   