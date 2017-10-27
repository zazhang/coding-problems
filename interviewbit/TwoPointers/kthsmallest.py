#!usr/bin/env ipython

"""Coding interview problem (array, math): 

See `https://www.interviewbit.com/problems/kth-smallest-element-in-the-array/`

Find the kth smallest element in an unsorted array of non-negative integers.

Definition of kth smallest element:
kth smallest element is the minimum possible n such that there are at least k elements in the array <= n.
In other words, if the array A was sorted, then A[k - 1] ( k is 1 based, while the arrays are 0 based ) 

NOTE:
You are not allowed to modify the array ( The array is read only ). 
Try to do it using constant extra space.

Example:

A : [2 1 4 3 2]
k : 3

answer : 2

"""
class Solution:
    # @param A : tuple of integers
    # @param k : integer
    # @return an integer
    # This implementation is slow, time limit exceeds
    def kthsmallest(self, A, k):
        if type(A) == int:
            return A
        else:
            temp_A = list(A)
        min_list = []
        index = 0
        while index < k: # k is 1 based, e.g. k=3 means 3 elements
            current_min = min(temp_A)
            min_list.append(current_min)
            temp_A.remove(current_min)
            index += 1
        return max(min_list)

    # This implementation uses extra space, not constant extra space
    def kthsmallest2(self, A, k):
        if type(A) == int:
            return A
        else:
            temp_A = list(A)
        temp_A.sort()
        return temp_A[k-1]

    # Need a method that is constant space and O(k) time
    def kthsmallest3(self, A, k):
        return None


if __name__ == '__main__':

    s = Solution() # create Solution object

    A = (1,3,2,234,5,6,1)
    k = 4
    print s.kthsmallest(A,k)
