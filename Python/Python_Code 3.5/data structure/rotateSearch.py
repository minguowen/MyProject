# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:35:49 2016

@author: Stranger
"""

class Solution():
    def rotateSearch(self,nums):
        '''求旋转后的最小值（无重复元素）
        '''
        L = len(nums)
        low = 0
        high = L-1
        while low<high:
            mid = (low+high)//2
            if nums[mid]>nums[high]:
                low = mid+1
            else:
                high = mid
        return nums[high]
    
    
    def rotateSearch2(self,nums):
        '''求旋转后的最小值（无重复元素）(错误版本)
        '''
        L = len(nums)
        low = 0
        high = L-1
        while low<high:
            mid = (low+high)//2
            if nums[mid]>nums[low]:
                low = mid+1
            else:
                high = mid
        return nums[high]
        
        
if __name__ == '__main__':
    a = Solution()
    nums = [4,5,6,7,0,1,2]
    res = a.rotateSearch2(nums)
        
        

            