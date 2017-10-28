#!usr/bin/env ipython

"""Coding interview problem (): 

Reverse integers

"""

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if isinstance(x, int) is True:
            num = x
            numlist = [str(i) for i in str(num)]
            reverselist = list(reversed(numlist))
            if reverselist[-1] is '-':
                sign = reverselist.pop(-1)
                reverselist.insert(0, sign)
            result = int(''.join(map(str, reverselist)))
            return result
        else:
            return 0
    # ? consider 10, 100
    # ? consider overflow, an integer is 32 bit

if __name__ == "__main__":
    a = Solution()
    print a.reverse(1)
