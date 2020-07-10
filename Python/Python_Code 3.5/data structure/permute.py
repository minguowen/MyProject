# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:48:27 2016

@author: Stranger
"""

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) == 0: return []
        if len(num) == 1: return [num]
        res = []
        for i in range(len(num)):
            for j in self.permute(num[:i] + num[i+1:]):
                res.append([num[i]] + j)
        return res
        
        
if __name__ == '__main__':
    a = Solution()
    num = [1,2,3]
    res = a.permute(num)