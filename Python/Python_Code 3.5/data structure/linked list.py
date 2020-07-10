# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 15:11:08 2016

@author: Stranger
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(ListNode):
    def reverse(self,head):
        pre = head
        cur = pre.next
        while cur:
            pre.next = cur.next
            cur.next = head
            head = cur
            cur = pre.next
        return head

    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        dummy = ListNode(0)
        dummy.next = head
        n = 0
        while dummy:
            dummy = dummy.next
            n +=1
        if n == 1:
            return True
        p = self.reverse(head)

        while head:
            if p.val != head.val:
                return False
            p = p.next
            head = head.next
        return True
        
        
        
        
