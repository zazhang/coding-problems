#!usr/bin/env ipython

"""Poisson Distribution I (statistics)

A random variable X, follows Poisson distribution with mean of 2.5. 
Find the probability with which the random variable X is equal to 5.

"""

import math


class Solution(object):
    def poissonDist(self, lam, k):
        """
        @param lam: float representing the lambda of poisson distribution
        @param k: int representing the actual number of events 
                  for poisson random variable 
        @return float denoting the probability, to 3 decimal place
        """
        f = lam**k * math.exp(-lam) / math.factorial(k)
        return round(f, 3)

    
if __name__ == '__main__':

    s = Solution()

    lam = float(raw_input())
    k = int(raw_input())
    print s.poissonDist(lam, k)