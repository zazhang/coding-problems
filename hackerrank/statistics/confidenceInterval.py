#!usr/bin/env ipython

"""Central Limit Theorem III (statistics)

You have a sample of 100 values from a population with mean 500 and with standard 
deviation 80. Compute the interval that covers the middle 95% of the distribution 
of the sample mean; in other words, compute A and B such that P(A<x<B)=0.95. 
Use the value of z=1.96.

"""

import math


class Solution(object):
    def confidenceInterval(self, mean, stdev, n, z):
        """
        @param mean: float representing the mean of normal distribution
        @param stdev: float representing the stdev of normal distribution
        @param n: int representing number of observations
        @param z: int representing z score
        @return a list of float denoting the lower and upper level of
            the confidence interval, to 2 decimal place
        Notes: p(x_bar - z*sigma/sqrt(n) < mu < x_bar + z*sigma/sqrt(n)) 
            = 0.95 for z = 1.96
        """
        L = mean - z*stdev/math.sqrt(n)
        U = mean + z*stdev/math.sqrt(n)
        return [round(L, 2), round(U, 2)]
        

if __name__ == '__main__':

    s = Solution()

    n = 100
    mean = 500
    stdev = 80
    prob = 0.95 # actually this number is not used, it is related to z
    z = 1.96
    res = s.confidenceInterval(mean, stdev, n, z)
    print res