#!usr/bin/env ipython

"""Coding interview problem (array): 

See `https://www.interviewbit.com/problems/inversions/`

Given an array A, count the number of inversions in the array.

Formally speaking, two elements `A[i]` and `A[j]` form an inversion if `A[i] > A[j]` and `i < j`

Example:

A : `[2, 4, 1, 3, 5]`
Output : `3`
as the `3` inversions are `(2, 1)`, `(4, 1)`, `(4, 3)`.

"""

class Solution:
    # Time complexity = O(n^2)
    # @param A : list of integers
    # @return an integer
    def countInversions(self, A):        
        cnt = 0
        for i in xrange(len(A)):
            for j in xrange(i, len(A)):
                if A[i] > A[j]:
                    cnt += 1
        return cnt

    # Hint: use merge sort to reduce the time complexity
    def countInversions2(self, A):
        return None


if __name__ == '__main__':

    s = Solution() # create Solution object

    A = [2,4,1,3,5]
    print s.countInversions(A)
