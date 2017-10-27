#!usr/bin/env ipython

"""Coding interview problem (array): 

Rotate an array a using positions given by b

E.g.
``a = [1,2,3,4,5,6]``
``b = 1``
``s.rotateArray(a,b)`` => [2,3,4,5,6,1]

"""
class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers    
    def rotateArray(self, a, b):
        ret = []
        for i in xrange(len(a)):
            move = b % len(a)
            if (i+move) >= len(a):
                ret.append(a[i + move - len(a)])
            else:
                ret.append(a[i + move])
        return ret

if __name__ == '__main__':

    s = Solution() # create Solution object

    a = [ 14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33, 96, 62, 32, 98, 77, 35 ]
    b = 56
    print s.rotateArray(a,b)    

