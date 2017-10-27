#!usr/bin/env ipython

"""Coding interview problem (linked list): 

See `https://www.interviewbit.com/problems/subtract/`

Given a singly linked list, modify the value of first half nodes such that :

1st node’s new value = the last node’s value - first node’s current value
2nd node’s new value = the second last node’s value - 2nd node’s current value,
and so on …

Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5,

You should return 4 -> 2 -> 3 -> 4 -> 5

Try to solve in constant extra space

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, node2):
        return self.val == node2.val and self.next == node2.next

    # Add a node from the end
    def add(self, node):
        self.next = node

    # !!! need to implement this function
    def removeAtEnd(self):
        return None


class Solution:
    # @param A: head node of linked list
    # @return the length of the linked list
    def getLength(self, A):
        length = 0
        while A != None:
            length += 1
            A = A.next
        return length

    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        l = self.getLength(A)
        fh = l / 2 # the first half nodes

        i = 0            
        while i < fh:
            cur = A
            tail = A          
            while tail.next != None:
                prev = tail
                tail = tail.next
            cur.val = tail.val - cur.val
            cur = cur.next
            # !!! add a line to remove the last node in A
            i += 1

            
        return None


if __name__ == '__main__':

    s = Solution() # create Solution object

    A = ListNode(1)
    A.next = ListNode(2)
    A.next.next = ListNode(3)
    A.next.next.next = ListNode(4)
    A.next.next.next.next = ListNode(5)
    #print s.subtract(A)
