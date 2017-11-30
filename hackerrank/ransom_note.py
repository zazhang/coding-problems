#!usr/bin/env ipython

"""Ransom Note (hash table)

A kidnapper wrote a ransom note but is worried it will be traced back to him. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use whole words available in the magazine, meaning he cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print `Yes` if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print `No`.

"""

import sys
from collections import defaultdict


def ransom_note(magazine, ransom):
    """This implementation is slow, O(n*m)
    @param magazine : a list of strings
    @param ransom : a list of strings
    @return boolean value
    """
    m = len(magazine)
    n = len(ransom)
    
    r = {}
    for i in xrange(m): # create a magazine words dict
        r[i] = magazine[i]

    for j in xrange(n):
        if ransom[j] in r.values(): # check if words in ransom are in the magazine
            for k,v in r.iteritems():
                if ransom[j] == v:
                    del r[k] # if yes, delete the magzine dict word
                    break
        else: return False # if no, cannot use magazine, return false
    #sys.stderr.write("final i is %s\n" %i)
    return True # otherwise, can use magazine, return true

def ransom_note2(magazine, ransom):
    """This is an answer implementation
    @param magazine : a list of strings
    @param ransom : a list of strings
    @return boolean value    
    """
    mdict = defaultdict(int)

    for word in magazine:
        mdict[word] += 1

    for word in ransom:
        if mdict[word] == 0: return False # if word not in mdict, still return 0
        else:
            mdict[word] -= 1

    return True
    

if __name__ == '__main__':
         
    """ # Read input from prompt
    m, n = map(int, raw_input().strip().split(' '))
    magazine = raw_input().strip().split(' ')
    ransom = raw_input().strip().split(' ')
    answer = ransom_note(magazine, ransom)
    if(answer):
        print "Yes"
    else:
        print "No"
    """

    # Read input from file
    filename = "input1.txt"
    with open( filename ) as f:        
        content = f.readlines()
        content = [x.strip() for x in content]
        #print content
        magazine = content[1].strip().split(' ')
        ransom = content[2].strip().split(' ')
        answer = ransom_note2(magazine, ransom)
        if(answer):
            print "Yes"
        else:
            print "No"
