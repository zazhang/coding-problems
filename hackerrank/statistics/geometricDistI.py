#!usr/bin/env ipython

"""Geometric Distribution I (statistics)

The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect is found during the 5th inspection?

"""

import math


class Solution(object):
    def geometricDist(self, numerator, denominator, n):
        """
        @param numerator: int representing numerator of defective p
        @param denominator: int representing denominator of defective p
        @param n: number of inspections
        @return float denoting the probability of 1st defect is found 
            during the 5th inspection
        """
        p = numerator / float(denominator)
        f = p**1*(1-p)**4
        return round(f,3)

    
if __name__ == '__main__':

    s = Solution()

    num = 1
    den = 3
    n = 5

    print s.geometricDist(num,den,n)
