#!usr/bin/env ipython

"""Balanced Brackets (stacks)
we say a sequence of brackets is considered to be balanced if the following 
conditions are met:
1. It contains no unmatched brackets.
2. The subset of brackets enclosed within the confines of a matched pair of 
brackets is also a matched pair of brackets.
Given  strings of brackets, determine whether each sequence of brackets 
is balanced. If a string is balanced, print YES on a new line; 
otherwise, print NO on a new line.
"""

# first, find the ascii code of six types of brackets
# second, write a matcher to pair brackets
# third, use stack to store the input string, pop from stack to create reverse string,
# fourth, for the input and reverse strings, check if ith position form a brackets
def is_matched(expression):
    """
    @param input: string
    @return bool
    """
    # use list as stack
    st = list()
    for i in expression:
        if i == '{' or i == '[' or i == '(':
            st.append(i)
        elif i == '}' or i == ']' or i == ')':
            if not st or is_pair(st.pop(), i) == False:
                return False
    if st:
        return False
    return True        

def is_pair(a, b):
    """
    @param a: char
    @param b: char
    @return bool
    """
    ascii_a = ord(a)
    ascii_b = ord(b)
    if ascii_a == 123 and ascii_b == 125: # { and }
        return True
    elif ascii_a == 125 and ascii_b == 123:
        return True
    elif ascii_a == 91 and ascii_b == 93: # [ and ]
        return True
    elif ascii_a == 93 and ascii_b == 91:
        return True
    elif ascii_a == 40 and ascii_b == 41: # ( and )
        return True
    elif ascii_a == 41 and ascii_b == 40:
        return True
    else:
        return False

if __name__ == '__main__':

    t = int(raw_input().strip())
    for a0 in xrange(t):
        expression = raw_input().strip()
        if is_matched(expression) == True:
            print "YES"
        else:
            print "NO"
