#!usr/bin/env ipython

"""Normal Distribution II (statistics)

The final grades for a Physics exam taken by a large group of students have 
a mean of 70 and a standard deviation of 10. If we can approximate the 
distribution of these grades by a normal distribution, what percentage of 
the students:

Scored higher than 80 (i.e., have a X > 80)?
Passed the test (i.e., have a X >= 60)?
Failed the test (i.e., have a X < 60)?

"""

import math


class Solution(object):
    def normalDist(self, mean, stdev, b, a=0):
        """
        @param mean: float representing the mean of normal distribution
        @param stdev: float representing the stdev of normal distribution
        @param b: float representing the upper bound of random variable X
        @param a: float representing the lower bound of random variable X
        @return float denoting the probability in percentage, 
            to 2 decimal place
        """
        phi_a = 0.5*(1+math.erf((a-mean)/(stdev*math.sqrt(2))))
        phi_b = 0.5*(1+math.erf((b-mean)/(stdev*math.sqrt(2))))
        p_b_minus_a = phi_b - phi_a
        res = round(p_b_minus_a,4)*100
        return res


if __name__ == '__main__':

    s = Solution()

    mean = 70
    stdev = 10
    b1 = 80
    b2 = 60
    res1 = s.normalDist(mean, stdev, b1)
    res2 = s.normalDist(mean, stdev, b2)
    print 100-res1
    print 100-res2
    print res2
