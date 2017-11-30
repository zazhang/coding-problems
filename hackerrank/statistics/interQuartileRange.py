#!usr/bin/env ipython

"""Find Interquartile Range (statistics)

Calculate interquartile range

"""

import math


class Solution(object):
    def calc_median(self, A):
        """
        @param A: a list of integers
        @return float denoting the median of the array, to 1 decimal place
        """
        if A == []:
            return 0        
        n = len(A)
        sort_A = sorted(A)
        if n % 2 == 0 and n != 1:
            mid = n / 2
            mid2 = mid - 1
            median = (sort_A[mid]+sort_A[mid2]) / 2.0
        else:
            mid = int(math.ceil(n / 2))
            median = sort_A[mid]
        return median * 1.0 # make it a float
    
    def quartiles(self, A):
        """
        @param A: a list of integers
        @return a list of floats denoting the quartiles
        """
        if A == []:
            return 0
        n = len(A)
        q2 = int(self.calc_median(A))
        sort_A = sorted(A)
        if n % 2 == 0:
            first_half = sort_A[:n/2]
            second_half = sort_A[n/2:]
        else:
            first_half = sort_A[:n/2]
            second_half = sort_A[n/2+1:]
        q1 = self.calc_median(first_half)
        q3 = self.calc_median(second_half)
        return [q1, q2, q3]

    def interQuartileRange(self, A, F):
        """
        @param A: a list of integers
        @param F: a list of integers representing frequencies of each
                  element in A
        @return float denoting the interquartile range, to 1 decimal place
        """
        n = len(A)
        S = []
        for i in xrange(n):
            S.append([A[i]]*F[i])
        flat_S = [item for sublist in S for item in sublist]
        res = self.quartiles(flat_S)
        return res[2] - res[0]


if __name__ == '__main__':

    s = Solution()

    A = [6,12,8,10,20,16]
    F = [5,4,3,2,1,5]
    A = [10, 40, 30, 50, 20, 10, 40, 30, 50, 20,
             1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    F = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 40,
             30, 50, 20, 10, 40, 30, 50, 20]
    #size = (raw_input())
    #numbers = list(map(int, raw_input().strip().split(' ')))
    #frequencies = list(map(int, raw_input().strip().split(' ')))
    print s.interQuartileRange(A,F)
