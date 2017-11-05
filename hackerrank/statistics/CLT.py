#!usr/bin/env ipython

"""Central Limit Theorem I (statistics)

A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of 205 pounds and a standard deviation of 15 pounds. Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?

"""

import math


class Solution(object):
    def CLT(self, mean, stdev, total_load, num_box):
        """
        @param mean: float representing the mean of normal distribution
        @param stdev: float representing the stdev of normal distribution
        @param total_load: int representing max weight load
        @param num_box: int representing number of boxes
        @return float denoting the probability transporting `num_box` boxes, 
            to 4 decimal place
        """
        sample_mean = mean*num_box
        sample_stdev = math.sqrt(num_box)*stdev
        p = self.normalDist(sample_mean, sample_stdev, total_load)
        return round(p, 4)


    def normalDist(self, mean, stdev, b, a=0):
        """
        @param mean: float representing the mean of normal distribution
        @param stdev: float representing the stdev of normal distribution
        @param b: float representing the upper bound of random variable X
        @param a: float representing the lower bound of random variable X
        @return float denoting the probability
        """
        phi_a = 0.5*(1+math.erf((a-mean)/(stdev*math.sqrt(2))))
        phi_b = 0.5*(1+math.erf((b-mean)/(stdev*math.sqrt(2))))
        p_b_minus_a = phi_b - phi_a
        return p_b_minus_a
        

if __name__ == '__main__':

    s = Solution()

    mean = 205
    stdev = 15
    max_weight = 9800
    num_box = 49
    res = s.CLT(mean, stdev, max_weight, num_box)
    print res
