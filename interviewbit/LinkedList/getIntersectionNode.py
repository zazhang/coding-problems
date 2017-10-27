#!usr/bin/env ipython

"""Coding interview problem (linked list): 

Write a program to find the node at which the intersection of two singly linked lists begins.

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, node2):
        return self.val == node2.val and self.next == node2.next

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list        
    def getIntersectionNode(self, A, B):
        m = self.getLength(A)
        n = self.getLength(B)
        if m >= n:
            d = m - n
        else:
            temp = A
            A = B
            B = temp
            d = n - m

        while d > 0:
            A = A.next
            d -= 1

        while A != None and B != None:
            if A == B: # without logical comparison, this won't work
                return A
            else:
                A = A.next
                B = B.next
        return None

    # @param A: head node of linked list
    # @return the length of the linked list
    def getLength(self, A):
        length = 0
        while A != None:
            length += 1
            A = A.next
        return length

    # This is the answer implementation
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        
        if A is None or B is None:
            return None
        
        m, n = 0, 0 # len(A) and len(B) respectively
        a, b = A, B
        while a is not None:
            m+= 1
            a= a.next
        while b is not None:
            n+= 1
            b= b.next
        
        swap= False
        if m < n:
            A, B = B, A
            m, n = n, m
            swap= False
        
        # { m      > n      }
        # { len(A) > len(B) }
        
        d= m - n
        a, b = A, B
        while d > 0:
            d-= 1
            a= a.next
        
        while a is not None:
            if a is b:
                if swap:
                    A, B = B, A
                return a
            a= a.next
            b= b.next
        
        if swap:
            A, B = B, A
        return None    


if __name__ == '__main__':

    s = Solution() # create Solution object

    A = ListNode(25)
    A.next = ListNode(97)
    A.next.next = ListNode(71)
    A.next.next.next = ListNode(83)
    A.next.next.next.next = ListNode(13)
    A.next.next.next.next.next = ListNode(36)
    A.next.next.next.next.next.next = ListNode(94)    
    B = ListNode(5)
    B.next = ListNode(83)
    B.next.next = ListNode(44)
    B.next.next.next = ListNode(36)
    B.next.next.next.next = ListNode(94)
    C = ListNode(1)
    D = ListNode(1)
    print C == D
    print s.getIntersectionNode(A,B).val
