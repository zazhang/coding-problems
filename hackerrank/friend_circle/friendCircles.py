#!usr/bin/env ipython

"""Firend Circles (graphs)

Two Sigma interview problem.

"""

import sys
import os


def friendCircles(friends):
    """
    @param friends: 2d-array of strings
    @return int denoting number of different friends circles
    
    This function uses a visited set to keep track 
        all the nodes that have been visited through dfs.
    """
    count = 0 # count the number of friend circles
    N = len(friends) # number of persons
    visited = set()

    for v in xrange(N): 
        if v not in visited: 

            # use dfs to find friend circles
            visit = [v] 
            while visit != []: 
                current = visit.pop() # current person to visit
                if current not in visited:
                    visited.add(current)
                    # for the current person,
                    #   find who should we visit next
                    for i in xrange(len(friends[current])): 
                        if friends[current][i] != 'N':
                            visit.append(i)
            count += 1
    return count


            
if __name__ == '__main__':

    A1 = [['Y','N','N'],['N','Y','N'],['N','N','Y']]
    A2 = [['Y','Y','N','N'],
          ['Y','Y','Y','N'],
          ['N','Y','Y','N'],
          ['N','N','N','Y']]
    print friendCircles(A2)
