#!usr/bin/env ipython

"""Coding interview problem (binary search): 

Given a sorted array of integers, find the number of occurrences of a given target value.
Your algorithm’s runtime complexity must be in the order of `O(log n)`.
If the target is not found in the array, return `0`

E.g.
``a = [1,2,2,3,4]``
``b = 2``
``s.findCount(a,b)`` => 2

"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer    
    def findCount(self, A, B):
        result = 0
        left_index = -1
        right_index = -1
        low = 0
        high = len(A) - 1
        while low <= high: # continue searching left
            mid = low + (high-low)/2
            if A[mid] == B:
                left_index = mid
                high = mid - 1
            elif A[mid] < B:
                    low = mid + 1
            else:
                high = mid - 1
        #print result_left

        low = 0
        high = len(A) - 1
        while low <= high: # continue searching right
            mid = low + (high-low)/2
            if A[mid] == B:
                right_index = mid
                low = mid + 1
            elif A[mid] < B:
                    low = mid + 1
            else:
                high = mid - 1
        #print result_right
        if left_index + right_index != -2:
            result = left_index - right_index + 1
        return result


if __name__ == '__main__':

    s = Solution() # create Solution object

    #A = (1,1,2,2,3,3,3,3,3,4,4,5,6,7,8,9)
    A = [1]
    B = 1
    print s.findCount(A,B)
