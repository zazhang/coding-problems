#!usr/bin/env ipython

"""Coding interview problem (math): 

Given 2 non negative integers `m` and `n`, find `gcd(m, n)`

GCD of 2 integers `m` and `n` is defined as the greatest integer `g` such that `g` is a divisor of both `m` and `n`.
Both `m` and `n` fit in a 32 bit signed integer.

E.g.
``A = 6``
``B = 9``
``s.gcd(A, B)`` => 3

"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer    
    def gcd(self, A, B):
        ret_A = []
        ret_B = []
        for i in range(1, int(math.ceil(math.sqrt(A)))+1):
            if A % i == 0:
                ret_A.append(i)
                if i != int(math.ceil(math.sqrt(A))):
                    ret_A.append(A/i)
        for i in range(1, int(math.ceil(math.sqrt(B)))+1):
            if B % i == 0:
                ret_B.append(i)
                if i != int(math.ceil(math.sqrt(B))):
                    ret_B.append(B/i)            
        ret = list(set(ret_A).intersection(set(ret_B)))
        ret.sort()
        if ret != []:
            return ret[-1]
        elif ret_A != [] and ret_B == []:
            return ret_A[-1]
        else:
            return ret_B[-1]


if __name__ == '__main__':

    s = Solution() # create Solution object

    A = 1
    B = 0
    print s.gcd(A)

