#!usr/bin/env ipython

"""Binomial Distribution I (statistics)

The ratio of boys to girls for babies born in Russia is 1.09:1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places

"""

import math


class Solution(object):
    def binomialDist(self, A, B):
        """
        @param A: int representing the first number of the ratio of babies
        @param B: int representing the second number of the ratio of babies
        @return float denoting the proportion of Russian families with 
            exactly 6 children will have at least 3 boys, 
            to 3 decimal place        
        """
        p = A / (A + B) # probability a baby is a boy
        q = 1 - p

        f = 0
        # combination 6C3
        for i in xrange(6,2,-1):
            c = self.combination(6, i)
            f += c*p**(i)*q**(6-i) # f(x) = nCx*p^x*(1-p)^x

        return round(f, 3)

    def combination(self, n, r):
        """
        @param n: int representing total number of elements
        @param r: int representing the number to select
        @return int denoting number of combinations
        """
        c = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
        return c
    
    
if __name__ == '__main__':

    s = Solution()

    A = 1.09
    B = 1

    print s.binomialDist(A,B)
