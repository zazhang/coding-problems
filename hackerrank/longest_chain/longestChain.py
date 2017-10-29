#!usr/bin/env ipython

"""Longest String Chain

Two Sigma interview problem.

"""

import sys
import os


def longestChain(w):
    """
    @param words: array of strings
    @return int denoting the length of the longest string chain
    
    This function uses a dictionary to store word as key,
        and chain length as value. Find the longest chain for 
        every word and return the maximum.    
    """
    if w == []:
        return 0
    count = {} # a dict to store (word : chainLength)
    words = set(w) # remove duplicates
    for word in words:
        findLongest(word, words, count)
    return max(count.values())

def findLongest(word, words, count):
    if word not in count:
        val = 1 # single character has a chain length of 1
        for i in xrange(len(word)):
            temp_word = word[:i] + word[i+1:] # exclude ith char
            
            if temp_word in words:
                # recursively find longest chain
                # if the `temp_word` is in the given array,
                #   increment `cnt` by 1
                # current `val` is the larger one between
                #   previous `val` and current `cnt`
                cnt = findLongest(temp_word, words, count)
                val = max(val, cnt+1)
                    
        count[word] = val # store val to the dict
    return count[word] # return the chain length of given word


if __name__ == '__main__':

    w1 = ['5', '44', '333', 'a', 'bs', 'bac', 'ba']
    w2 = ['6','a','b','ba','bca','bda','bdca']
    w3 = [ "bdcafg", "bdcaf", "a",  "b",  "ba", "bca", "bda", "bdca" ]
    w4 = ['1','1a','aaac1']
    w5 = ['1','2','3']
    w6 = []
    print longestChain(w3)
