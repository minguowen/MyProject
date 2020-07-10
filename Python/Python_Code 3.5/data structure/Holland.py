# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:28:52 2016

@author: Stranger
"""

class Solution():
    def Holland(self,nums):
        L = len(nums)
        if L == 0 or L == 1:
            return nums
        nums = list(nums)
        begin = 0
        end = L - 1
        cur = 0
        while cur != end:
            if nums[cur] == '0':
                if cur == begin:
                    cur+=1
                    begin+=1
                else:
                    nums[begin],nums[cur] = nums[cur],nums[begin]
                    begin+=1
            elif nums[cur] == '2':
                nums[cur],nums[end] = nums[end],nums[cur]
                end-=1
            else:
                cur+=1
        "".join(nums)
        return nums
                
                
                
                
if __name__ == '__main__':
    a = Solution()
    nums = '222222111111020220'
    res = a.Holland(nums)
