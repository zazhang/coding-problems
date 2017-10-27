#!usr/bin/env ipython

"""Coding interview problem (bit manipulation): 

Reverse bits of an 32 bit unsigned integer

Example 1:

x = 0,

          00000000000000000000000000000000  
=>        00000000000000000000000000000000
return `0`

Example 2:

x = 3,

          00000000000000000000000000000011 
=>        11000000000000000000000000000000
return `3221225472`

"""
class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        string_A = format(A, '032b')
        new_A = "".join(list(reversed(string_A)))
        num_int = int(new_A, 2)
        return num_int

    def check_state_at_position(self, x, position):
        mask = 1 << position
        return x & mask != 0
    
    def set_state_at_position(self, x, position, state):
        mask = 1 << position
        return (x & ~mask) | (-state & mask)
    
    def reverse2(self, x):
        for i in range(32 / 2):
            left_state = self.check_state_at_position(x, 32 - 1 - i)
            right_state = self.check_state_at_position(x, i)
            
            x = self.set_state_at_position(x, i, left_state)
            x = self.set_state_at_position(x, 32 - 1 - i, right_state)
        
        return x


if __name__ == '__main__':

    s = Solution() # create Solution object

    A = ( 12, 30, 41, 51, 56, 58, 63, 67, 82, 90, 93 )
    B = ( 7, 9, 17, 17, 19, 21, 26, 34, 65, 65, 67, 68, 71, 75, 92 )
    print s.intersect(A,B)
