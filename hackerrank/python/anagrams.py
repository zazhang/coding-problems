#!usr/bin/env ipython

""" Anagrams (strings)

Given two strings, `a` and `b`, that may or may not be the same length, 
determine the minimum number of character deletions required to make 
`a` and `b` anagrams. Any characters can be deleted from either 
of the strings.

"""

from collections import Counter

def anagrams(a, b):
    """
    @param a : a string
    @param b : a string
    @return int
    """
    count_a = dict(Counter(list(a)))
    count_b = dict(Counter(list(b)))
    # find common items in two dict
    common = set(count_a).intersection(set(count_b))
    # find difference between two dict
    uncommon_b = { k : count_b[k] for k in set(count_b) - set(count_a) }
    uncommon_a = { k : count_a[k] for k in set(count_a) - set(count_b) }    

    result = sum(uncommon_a.values()) + sum(uncommon_b.values())

    num = 0
    for i in common:
        temp_a = count_a.get(i)
        temp_b = count_b.get(i)
        if temp_a != temp_b:
            num += abs(temp_a - temp_b)
    result = result + num
    
    return result
    
    
if __name__ == '__main__':

    # Read input from prompt
    a = raw_input().strip().split(' ')
    b = raw_input().strip().split(' ')
    answer = anagrams(a, b)
    print answer

