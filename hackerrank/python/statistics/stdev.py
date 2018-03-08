#!usr/bin/env ipython

"""Find Standard Deviation (statistics)

Calculate standard deviation

"""

import math


class Solution(object):
    def calc_mean(self, A):
        """
        @param A: a list of integers
        @return float denoting the mean of the array, to 1 decimal place
        """
        n = round(len(A),1) # round to 1 decimal
        sum_num = sum(A)
        res = sum_num / n

        return res
    
    def stdev(self, A):
        """
        @param A: a list of integers
        @return float denoting the stdev of the array, to 1 decimal place
        """
        n = len(A)
        mean = self.calc_mean(A)
        diff_square = [(a-mean)**2 for a in A]
        sum_diff_square = sum(diff_square)

        sigma = math.sqrt(sum_diff_square/n)
        return round(sigma, 1)

            
if __name__ == '__main__':

    s = Solution()

    numbers = [10, 40, 30, 50, 20]
    #size = (raw_input())
    #numbers = list(map(int, raw_input().strip().split(' ')))
    print s.stdev(numbers)
