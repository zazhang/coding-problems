#!usr/bin/env ipython

"""Normal Distribution I (statistics)

In a certain plant, the time taken to assemble a car is a random variable, X, 
having a normal distribution with a mean of 20 hours and a standard deviation 
of 2 hours. What is the probability that a car can be assembled at this plant in:

Less than 19.5 hours?
Between 20 and 22 hours?

"""

import math


class Solution(object):
    def normalDist(self, mean, stdev, b, a=0):
        """
        @param mean: float representing the mean of normal distribution
        @param stdev: float representing the stdev of normal distribution
        @param b: float representing the upper bound of random variable X
        @param a: float representing the lower bound of random variable X
        @return float denoting the probability, to 3 decimal place
        """
        phi_a = 0.5*(1+math.erf((a-mean)/(stdev*math.sqrt(2))))
        phi_b = 0.5*(1+math.erf((b-mean)/(stdev*math.sqrt(2))))
        p_b_minus_a = phi_b - phi_a
        return round(p_b_minus_a,3)


if __name__ == '__main__':

    s = Solution()

    #line1 = list(map(float, raw_input().strip().split(' ')))
    #b1 = float((raw_input()))
    #line2 = list(map(float, raw_input().strip().split(' ')))
    #res1 = s.normalDist(line1[0], line1[1], b1)
    #res2 = s.normalDist(line1[0], line1[1], line2[1], line2[0])
    mean = 20
    stdev = 2
    b1 = 19.5
    a = 20
    b = 22
    res1 = s.normalDist(mean, stdev, b1)
    res2 = s.normalDist(mean, stdev, b, a)
    print res1
    print res2
