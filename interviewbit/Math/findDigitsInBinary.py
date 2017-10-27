#!usr/bin/env ipython

"""Coding interview problem (math): 

Given a number `N >= 0`, find its representation in binary

E.g.
``A = 14``
``s.findDigitsInBinary(A)`` => 1110

"""
class Solution:
    # @param A : integer
    # @return a string    
    def findDigitsInBinary(self, A):
        ret = []
        if A == 0:
            return '0'
        else:
            while A > 0:
                rem = A % 2
                ret.append(str(rem))
                A = A / 2
            ret = list(reversed(ret))
            string_ret = ''.join(ret)
            return string_ret

if __name__ == '__main__':

    s = Solution() # create Solution object

    A = 14
    print s.findDigitsInBinary(A)

