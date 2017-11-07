#!usr/bin/env ipython

"""Pearson Correlation Coefficient (statistics)

Given two n-element data sets, A and B, calculate the value of the Pearson 
correlation coefficient.

"""

import math


class Solution(object):
    def calc_mean(self, A):
        """
        @param A: a list of integers
        @return float denoting the mean of the array
        """
        n = float(len(A))
        sum_num = sum(A)
        res = sum_num / n

        return res

    def stdev(self, A, mean):
        """
        @param A: a list of integers
        @return float denoting the stdev of the array

        """
        n = len(A)
        diff_square = []
        for i in xrange(n):
            diff_square.append((A[i] - mean)**2)
        sum_diff_square = sum(diff_square)

        sigma = math.sqrt(sum_diff_square/n)
        return sigma

    def pearsonCorrelation(self, A, B):
        """
        @param A: a list of float
        @param B: a list of float
        @return float denoting the stdev of the array, to 3 decimal place
        """
        n = len(A)
        mean_A = self.calc_mean(A)
        mean_B = self.calc_mean(B)
        stdev_A = self.stdev(A, mean_A)
        stdev_B = self.stdev(B, mean_B)
        sum_diff = 0
        for i in xrange(n):
            sum_diff += (A[i]-mean_A)*(B[i]-mean_B)
        rho = sum_diff/(n*stdev_A*stdev_B)
        return round(rho, 3)

if __name__ == '__main__':

    s = Solution()

    n = float(raw_input())
    A = list(map(float, raw_input().strip().split(' ')))
    B = list(map(float, raw_input().strip().split(' ')))
    res = s.pearsonCorrelation(A,B)
    print res
