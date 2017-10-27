#!usr/bin/env ipython

"""Coding interview problem (binary search): 

Implement `int sqrt(int x)`.

Compute and return the square root of `x`.

If `x` is not a perfect square, return `floor(sqrt(x))`

E.g.
Input : 11
Output : 3

"""
class Solution:
    # This implementation runs slow, b/c the range()
    # @param A : integer
    # @return an integer    
    def sqrt(self, A):
        digits = len(str(A))
        if digits > 1:
            lis = range(0, 10**(digits/2+1))
        else:
            lis = range(0, A+1)
        n = len(lis)
        low = 0
        high = n - 1
        while low <= high:
            mid = low + (high - low) / 2
            if lis[mid]**2 == A:
                return lis[mid]
            elif lis[mid]**2 <= A:
                low = mid + 1
            elif lis[mid]**2 >= A:
                high = mid - 1
        if low > high:
            return lis[high]

    # This is my implementation that passes the tests
    # @param A : integer
    # @return an integer
    def sqrt2(self, A):
        if A == 0: return 0
        low = 1
        high = A
        while low <= high:
            mid = low + (high - low) / 2
            if mid**2 == A:
                return mid
            elif mid**2 <= A:
                low = mid + 1
            elif mid**2 >= A:
                high = mid - 1
        if low > high:
            return high

    # This is the answer implementation
    # @param A : integer
    # @return an integer    
    n=0
    a=0
    def sqrt3(self, A):
        if self.a == A: return self.n
        else: self.a=A
        mid = 1
        lo = 1
        hi = A
        while lo < hi:
            mid = lo + (hi-lo)//2
            midval = mid*mid
            #print midval, self.n
            if midval < A:
                lo = mid+1
            elif midval > A: 
                hi = mid
            else:
                return mid
                
        if mid*mid>A: mid-=1 # deals with non-perfect sqrt
        self.n = mid
        #print "!!!", lo, hi, mid 
        return mid


if __name__ == '__main__':

    s = Solution() # create Solution object

    A = 253234243243
    print s.sqrt2(A)
