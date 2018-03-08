#!usr/bin/env ipython

"""Find Mean, Median, Mode (statistics)

Calculate mean, median, mode

"""

from collections import defaultdict


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

    def calc_median(self, A):
        """
        @param A: a list of integers
        @return float denoting the median of the array, to 1 decimal place
        """
        if A == []:
            return 0        
        n = len(A)
        sort_A = sorted(A)
        if n % 2 == 0 and n != 1:
            mid = n / 2
            mid2 = mid - 1
            median = (sort_A[mid]+sort_A[mid2]) / 2.0
        else:
            mid = int(math.ceil(n / 2))
            median = sort_A[mid]
        return median

    def calc_mode(self, A):
        """
        @param A: a list of integers
        @return float denoting the mode of the array, to 1 decimal place
        """        
        res = []
        d = defaultdict(int)
        for k in A:
            d[k] += 1
        max_val = max(d.values())
        for k,v in d.iteritems():
            if v == max_val:
                res.append(k)
        return min(res)

            
if __name__ == '__main__':

    s = Solution()

    A = [64630, 11735, 14216, 99233, 14470,
             4978, 73429, 38120, 51135, 67060]

    # read stdin input using raw_input()
    #size = int(raw_input())
    #numbers = list(map(int, raw_input().strip().split(' ')))        
    print 'mean is %s' %s.calc_mean(A)
    print 'median is %s' %s.calc_median(A)
    print 'mode is %s' %s.calc_mode(A)
