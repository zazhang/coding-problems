#!usr/bin/env ipython

"""Coding interview problem (linked list, recursion): 

Reverse a linked list using recursion.

Example :
given 1->2->3->4->5->NULL,

return 5->4->3->2->1->NULL.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # A recursive implementation
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        if A.next == None:
            return A
        
        prev = A
        A = A.next
        res = self.reverseList(A)
        A.next = prev
        prev.next = None
        return res

    # This is a non-recursive implementation
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList2(self, A):
        prev = None
        current = A
        while current != None:
            ne = current.next
            current.next = prev
            prev = current
            current = ne
        return prev


if __name__ == '__main__':

    s = Solution() # create Solution object

    A = ListNode(1)
    A.next = ListNode(2)
    A.next.next = ListNode(3)
    print s.reverseList(A).next.val
