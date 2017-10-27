#!usr/bin/env ipython

"""Coding interview problem (array): 

Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

E.g.
``A = ([1,2,3],[4,5,6],[7,8,9])``
``s.spiralOrder(A)`` => [1,2,3,6,9,8,7,4,5]

"""
class Solution:
    # @param A : a tuple of lists of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        m = len(A) # number of row
        n = len(A[0]) # number of column
        t = 0; b=m-1; l=0; r=n-1
        direction = 0 # directions: 0-right, 1-down, 2-left, 3-up

        while t <= b and l <= r:
            if direction == 0:
                for i in range(l,r+1):
                    print "dir0: %s" %i
                    result.append(A[t][i])
                t += 1
                direction = 1
            elif direction == 1:
                for i in range(t,b+1):
                    print "dir1: %s" %i
                    result.append(A[i][r])
                r -= 1
                direction = 2
            elif direction == 2:
                for i in range(r,l-1,-1):
                    print "dir2: %s" %i
                    result.append(A[b][i])
                b -= 1
                direction = 3
            elif direction == 3:
                for i in range(b,t-1,-1):
                    print "dir3: %s" %i                
                    result.append(A[i][l])
                l += 1
                direction = 0

        return result

if __name__ == '__main__':

    s = Solution() # create Solution object
    
    A = ([1,2,3],[4,5,6],[7,8,9])
    print s.spiralOrder(A)
