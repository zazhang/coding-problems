#!usr/bin/env ipython

"""Coding interview problem (array, math): 

Print concentric rectangular pattern in a 2d matrix. 
Let us show you some examples to clarify what we mean.

E.g.
Input: A = 4.
Output:

4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 

Input: A = 3.
Output:

3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3

"""
class Solution:
    # This problem is similar to spiralOrder
    # @param A : integer
    # @return a list of list of integers    
    def prettyPrint(self, A):
        size = 2*A-1
        res = [[0] * size for i in range(size)]
        t = 0
        b = size - 1
        l = 0
        r = size - 1

        while t <= b and l <= r:
            for i in range(l,r+1):
                res[t][i] = A
            t += 1
            for i in range(t, b+1):
                res[i][r] = A
            r -= 1
            for i in range(r, l-1, -1):
                res[b][i] = A
            b -= 1
            for i in range(b, t-1, -1):
                res[i][l] = A
            l += 1
            A -= 1
        return res


if __name__ == '__main__':

    s = Solution() # create Solution object

    A = 1
    B = 0
    print s.gcd(A)
