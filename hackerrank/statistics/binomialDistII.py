#!usr/bin/env ipython

"""Binomial Distribution II (statistics)

A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

1. No more than 2 rejects?
2. At least 2 rejects?

"""

import math


class Solution(object):
    def binomialDist(self, p, n):
        """
        @param p: int representing precentage of defective pistons
        @param n: int representing the size of the current batch of pistons
        @return a list of float denoting the answer of no more than 2 
            rejects, and the answer of at least 2 rejects
        """
        p = p/100.0
        # answer for at least 2
        f1 = 0        
        for i in xrange(3):
            c = self.combination(n, i)
            f1 += c*p**(i)*(1-p)**(n-i) # f(x) = nCx*p^x*(1-p)^x

        f2 = 0        
        for i in xrange(n, 1, -1):
            c = self.combination(n, i)
            f2 += c*p**(i)*(1-p)**(n-i) # f(x) = nCx*p^x*(1-p)^x
        
        return [round(f1,3), round(f2,3)]
        
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

    A = 12
    B = 10

    print s.binomialDist(A,B)
