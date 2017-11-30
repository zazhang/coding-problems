#!usr/bin/env ipython

"""Find Weighted Mean (statistics)

Calculate weighted mean

"""


class Solution(object):
    def weightedMean(self, A, W):
        """
        @param A: a list of integers
        @param W: a list of integers representing weights
        @return float denoting the weighted mean of the array, to 1 decimal place
        """
        n = len(A)
        if n == []:
            return 0
        
        sum_weights = sum(W)
        """
        prod = []
        for i in xrange(n):
            prod.append(A[i]*W[i])
        """
        prod = [a*w for a, w in zip(A, W)] # a simpler implementation
        sum_prod = sum(prod)
        res = sum_prod * 1.0 / sum_weights

        return round(res, 1)

            
if __name__ == '__main__':

    s = Solution()

    numbers = [1,3,5]
    weights = [2,4,6]
    print s.weightedMean(numbers, weights)    
