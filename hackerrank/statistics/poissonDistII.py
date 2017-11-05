#!usr/bin/env ipython

"""Poisson Distribution II (statistics)

The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:

The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating A is C_A = 160+40*X^2.
The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. The daily cost of operating B is C_B = 128+40*Y^2.

"""

import math


class Solution(object):
    def poissonDist(self, lam1, lam2):
        """
        @param lam1: float representing the lambda of 1st poisson distribution
        @param lam2: float representing the lambda of 2nd poisson distribution
        @return a list of float denoting the cost of A and B, to 3 
            decimal place
        """
        
        ca = 160+40*(lam1+lam1**2)
        cb = 128+40*(lam2+lam2**2)
        return [round(ca,3), round(cb,3)]

    
if __name__ == '__main__':

    s = Solution()

    #numbers = list(map(float, raw_input().strip().split(' ')))
    #lam1 = numbers[0]
    #lam2 = numbers[1]
    lam1 = 0.88
    lam2 = 1.55
    res = s.poissonDist(lam1, lam2)
    print res[0]
    print res[1]
