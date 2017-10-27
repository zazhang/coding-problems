#!usr/bin/env ipython

"""Coding interview problem (math): 

Given a non negative integer A, 
following code tries to find all pair of integers (a, b) such that:

`a` and `b` are positive integers
`a <= b`, and
`a2 + b2 = A`
`0 <= A <= 100000`

"""
class Solution:
    # @param A : integer
    # @return a list of list of integers    
    def squareSum(self, A):
        ans = []
        a = 0
        if A >= 0 and A <= 100000:
            while a * a < A:
                b = a
                while b * b < A:
                    if a * a + b * b == A and a <= b:
                        newEntry = [a, b]
                        ans.append(newEntry)
                    b += 1
                a += 1
        return ans

if __name__ == '__main__':

    s = Solution() # create Solution object

    A = 25
    print s.squareSum(A)    

