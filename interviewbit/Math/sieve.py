#!usr/bin/env ipython

"""Coding interview problem (math): 

Return all prime numbers up to N

E.g.
``A = 15``
``s.sieve(A)`` => [2,3,5,7,11,13]

"""
class Solution:
    # @param A : integer
    # @return a list of integers      
    def sieve(self, A):    
        num = range(A+1)
        primes = [1] * (A+1)
        primes[0] = 0
        #num.pop(0) # remove 0 from num
        primes[1] = 0
        #num.pop(0) # remove 1 from num, it is now the first element in num
        for i in range(2,int(math.ceil(math.sqrt(A)))+1):
            if primes[i] == 1:
                for j in range(2, A):
                    if i*j <= A:
                        primes[i*j] = 0
        ret = [i*j for i,j in zip(num,primes)]
        ret = list(filter(lambda x: x != 0, ret))
        return ret

if __name__ == '__main__':

    s = Solution() # create Solution object

    A = 15
    print s.sieve(A)

