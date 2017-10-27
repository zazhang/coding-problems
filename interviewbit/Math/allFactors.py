#!usr/bin/env ipython

"""Coding interview problem (math): 

Return all factors of a number

E.g.
``A = 6``
``s.allFactors(A)`` => [1,2,3,6]

"""
class Solution:
    # @param A : integer
    # @return a list of integers        
    def allFactors(self, A):    
        ret = []
        for i in range(1, int(math.ceil(math.sqrt(A)))+1):
            if A % i == 0:
                ret.append(i)
                if i!= int(math.ceil(math.sqrt(A))):
                    ret.append(A/i)
        ret = list(set(ret))
        ret.sort()
        return ret

if __name__ == '__main__':

    s = Solution() # create Solution object

    A = 0
    print s.allFactors(A)    

