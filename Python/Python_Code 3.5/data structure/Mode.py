# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 22:31:12 2016

@author: Stranger
"""

class Solution():
    def Mode(self,nums):
        '''众数一定存在的情况
        '''
        L = len(nums)
        m = nums[0]
        count = 1
        for i in range(1,L):
            if count == 0:
                m = nums[i]
                count=1
            else:
                if m!=nums[i]:
                    count-=1
                else:
                    count+=1
        return m

if __name__ == '__main__':
    a = Solution()
    nums = [1,2,3,1,4,1,2,1,1]
    res = a.Mode(nums)
          
            
            