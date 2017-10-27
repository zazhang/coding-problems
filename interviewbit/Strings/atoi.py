#!usr/bin/env ipython

"""Coding interview problem (strings): 

Implement atoi to convert a string to an integer.

Example :

Input : "9 2704"
Output : 9

Note: 
1. clean whitespace before string
2. take sign of a number
3. ignore any invalid character inside the string
4. handle overflow int

"""
class Solution:
    def check_and_return(self, res):
        res = int("".join(res))
        if res > (2**31 -1):
            return 2**31-1
        elif res < -2**31:
            return -2**31
        return res

    # @param A : string
    # @return an integer
    def atoi(self, A):
        res = []
        no_leading_space = A.strip()
        
        if no_leading_space[0] == '-' or no_leading_space[0] == '+':
            if len(A) == 1 or not no_leading_space[1].isdigit():
                return 0
            else: 
                res.append(no_leading_space[0])
                for i in no_leading_space[1:]:
                    if i.isdigit():
                        res.append(i)
                    elif i == ' ' or not i.isdigit():
                        return self.check_and_return(res)
        elif not no_leading_space[0].isdigit():
            return 0
        else:
            for i in no_leading_space:
                if i.isdigit():
                    res.append(i)
                elif i == ' ' or not i.isdigit():
                    return self.check_and_return(res)
                
        return self.check_and_return(res)

    # This is the answer implementation
    def atoi2(self, s):
        s = s.strip() # strips all spaces on left and right
        if not s: return 0
        sign = -1 if s[0] == '-' else 1
        val, index = 0, 0
        if s[0] in ['+', '-']: index = 1
        while index < len(s) and s[index].isdigit():
            val = val*10 + ord(s[index]) - ord('0') # assumes there're no invalid chars in given string
            index += 1
        #return sign*val
        return max(-2**31, min(sign * val,2**31-1))


if __name__ == '__main__':

    s = Solution() # create Solution object

    A = "5121478262 8070067M75 X199R 547 8C0A11 93I630 4P4071 029W433619 M3 5 14703818 776366059B9O43393"
    print s.atoi(A)

