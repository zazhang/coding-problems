#!usr/bin/env ipython

"""Spearman Correlation Coefficient (statistics)

Given two n-element data sets, X and Y, calculate the value of Spearman's 
rank correlation coefficient.

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
        @return float denoting the stdev of the array
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
        return rho

    def rankdata(self, X):
        """
        @param X: a list of float
        @return a list of int denoting the rank of the list
        Notes: this implemention gets a different result comparing with 
            scipy.stats.rankdata()
        """
        x_rank = dict((x, i+1) for i, x in enumerate(sorted(set(X))))
        return [x_rank[x] for x in X]

    def spearmanRankCorrelation(self, A, B):
        """
        @param A: a list of float
        @param B: a list of float
        @return float denoting the stdev of the array, to 3 decimal place
        """
        rank_A = self.rankdata(A)
        rank_B = self.rankdata(B)
        if len(A) == len(set(A)) and len(B) == len(set(B)):
            # only if all elements are distinct, apply the formula
            n = len(A)
            d_square = 0
            for i in xrange(n):
                d_square += (rank_A[i]-rank_B[i])**2
            r = 1 - (6.0 * d_square)/(n * (n * n - 1))
        else: 
            r = self.pearsonCorrelation(rank_A, rank_B)
        return round(r, 3)
    

if __name__ == '__main__':

    s = Solution()

    A = [10, 9.8, 8, 7.8, 7.7, 1.7, 6, 5, 1.4, 2]
    B = [200, 44, 32, 24, 22, 17, 15, 12, 8, 4]
    C = [0.2,1.3,0.2,1.1,1.4,1.5]
    D = [1.9,2.2,3.1,1.2,2.2,2.2]
    res = s.spearmanRankCorrelation(C,D)
    print res
