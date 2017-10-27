#!usr/bin/env ipython

"""Coding interview problem (array): 

Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has `[1, 2, 3]`

the returned vector should be `[1, 2, 4]`

as `123 + 1 = 124`.

"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    res = []
    def plusOne(self, A):
        if A == []:
            A.append(1)
            self.res = A + self.res
            return self.res
        
        temp = A[-1]
        if temp < 9:
            A[-1] = temp + 1
            self.res = A + self.res
            while self.res[0] == 0:
                self.res.pop(0)
            return self.res
        elif temp == 9:
            A[-1] = 0
            self.res = [A.pop()] + self.res
            return self.plusOne(A)

    # This is the answer implementation, no recursion
    # @param A : list of integers
    # @return a list of integers
    def plusOne2(self, A):
        while(A[0]==0)and len(A)>1:
            del(A[0])
        if A[0]==0 and len(A)==1:
            A[0]=1
            return A
        i=len(A)-1
        carry=1 # use carry to make it flexible to add any number
        while True:
            value=A[i]+carry
            if value>=10:
                A[i]=value%10
                carry=value//10
            else:
                A[i]=value
                break
            if i==0:
                A.insert(0,carry)
                break
            i-=1
        return A


if __name__ == '__main__':

    s = Solution() # create Solution object

    A = [0,0,9,9,9,9,9]
    print s.plusOne(A)

