#!usr/bin/env ipython

"""Coding interview problem (queue): 

Given an array, find the next greater element G[i] for every element A[i] in the array. The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array. 
More formally,

G[i] for an element A[i] = an element A[j] such that 
    j is minimum possible AND 
    j > i AND
    A[j] > A[i]
Elements for which no greater element exist, consider next greater element as -1.

Example:

Input : A : [4, 5, 2, 10]
Output : [5, 10, 10, -1]

Example 2:

Input : A : [3, 2, 1]
Output : [-1, -1, -1]

"""

from collections import deque
    
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        res = []
        a = deque(A)
        for i in xrange(len(a)):
            j = i + 1
            while j < len(a):
                if a[j] > a[i]:
                    res.append(a[j])
                    break
                else:
                    j += 1
            if j >= len(a):
                res.append(-1)
        return res


if __name__ == '__main__':

    s = Solution() # create Solution object

    A = [3, 2, 1]
    print s.nextGreater(A)
