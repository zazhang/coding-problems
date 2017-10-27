#!usr/bin/env ipython

"""Coding interview problem (stack): 

Given a string S, reverse the string using stack.

Example:

Input : "abc"
Return "cba"

"""


class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        s = []
        res = list(A)
        for i in A:
            s.append(i)
        for i in range(len(A)):
            res[i] = s[-1]
            s.pop()
        return "".join(res)


if __name__ == '__main__':

    s = Solution() # create Solution object

    A = 'dne'
    print s.reverseString(A)
