#!usr/bin/env ipython

"""Find Quartiles (statistics)

Calculate quartiles

"""

class Solution(object):
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
            mid = n / 2
            median = sort_A[mid]
        return median
    
    def quartiles(self, A):
        """
        @param A: a list of integers
        @return a list of integers denoting the quartiles
        """
        if A == []:
            return 0
        n = len(A)
        q2 = int(self.calc_median(A))
        sort_A = sorted(A)
        if n % 2 == 0:
            first_half = sort_A[:n/2]
            second_half = sort_A[n/2:]
        else:
            first_half = sort_A[:n/2]
            second_half = sort_A[n/2+1:]
        q1 = self.calc_median(first_half)
        q3 = self.calc_median(second_half)
        return [q1, q2, q3]


if __name__ == '__main__':

    s = Solution()

    numbers = [7, 8, 5, 12, 14, 21, 13]
    test1 = [7, 15, 36, 39 ,40, 41]
    test2 = [10, 3, 7, 8, 5, 12, 14, 21, 15, 18, 14]
    test3 = [12, 4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 12]
    #size = (raw_input())
    #numbers = list(map(int, raw_input().strip().split(' ')))
    print s.quartiles(test2)
