#!usr/bin/env ipython

"""Coding interview problem (math): 

Check if a number is a prime number, return `1` if yes, and `0` otherwise

E.g.
``A = 13``
``s.isPrime(A)`` => 1

"""
class Solution:
    # @param A : integer
    # @return an integer, 1 means prime, 0 means non-prime       
    def isPrime(self, A):     
        if A == 1:
            return 0
        else:
            for i in range(2, int(math.ceil(math.sqrt(A)))+1):
                if A % i == 0:
                    return 0
        return 1

if __name__ == '__main__':

    s = Solution() # create Solution object

    A = 14
    print s.isPrime(A)    

