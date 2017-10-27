#!usr/bin/env ipython

"""Coding interview problem (array): 

See `https://www.interviewbit.com/problems/longest-consecutive-sequence/`

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example: 
Given `[100, 4, 200, 1, 3, 2]`,
The longest consecutive elements sequence is `[1, 2, 3, 4]`. Return its length: `4`.

Your algorithm should run in `O(n)` complexity.

"""
class Solution:
    # A simple array implementation
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        res = []
        # check corner cases
        if A == None:
            return 0
        elif len(A) == 1:
            return 1
        
        A = list(set(A))
        A.sort()
        i = 0
        temp = []
        while i < len(A) - 1:
            if A[i+1] - A[i] == 1:
                temp.append(A[i])
                temp.append(A[i+1])
                i += 1
            else:
                temp = list(set(temp))
                if len(temp) > len(res):
                    res = temp
                temp = []
                i += 1
        temp = list(set(temp))
        if len(temp) > len(res):
            res = temp
        if len(res) == 0: # if does not find more than one consecutive numbers
            return 1 
        return len(res)

    # !!! May implement using recursion
    def longestConsecutive2(self, A):
    	return None



if __name__ == '__main__':

    s = Solution() # create Solution object

    A = (1,)
    A = ( 97, 86, 67, 19, 107, 9, 8, 49, 23, 46, -4, 22, 72, 4, 57, 111, 20, 52, 99, 2, 113, 81, 7, 5, 21, 0, 47, 54, 76, 117, -2, 102, 34, 12, 103, 69, 36, 51, 105, -3, 33, 91, 37, 11, 48, 106, 109, 45, 58, 77, 104, 60, 75, 90, 3, 62, 16, 119, 85, 63, 87, 43, 74, 13, 95, 94, 56, 28, 55, 66, 92, 79, 27, 42, 70 )
    A = (2,3,6,4,7,8,9)
    A = (1,1,2,2,3,3,4,4,5,5)
    A = (51,40)
    print s.longestConsecutive(A)
