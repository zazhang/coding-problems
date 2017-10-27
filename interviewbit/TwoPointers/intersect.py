#!usr/bin/env ipython

"""Coding interview problem (two pointers): 

Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]

"""
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        res = []
        n = len(A)
        m = len(B)
        i = 0
        j = 0
        while i < n and j < m:
                if A[i] > B[j]:
                    j += 1
                elif A[i] < B[j]:
                    i += 1
                elif A[i] == B[j]:
                    res.append(A[i])
                    i += 1
                    j += 1    
        return res

if __name__ == '__main__':

    s = Solution() # create Solution object

    A = ( 12, 30, 41, 51, 56, 58, 63, 67, 82, 90, 93 )
    B = ( 7, 9, 17, 17, 19, 21, 26, 34, 65, 65, 67, 68, 71, 75, 92 )
    print s.intersect(A,B)
