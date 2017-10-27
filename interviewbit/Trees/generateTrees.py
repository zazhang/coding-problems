#!usr/bin/env ipython

"""Coding interview problem (trees): 

See `https://www.interviewbit.com/problems/unique-binary-search-trees/`

Given A, generate all structurally unique BST’s (binary search trees) that store values `1...A`.

Example : 
Given A = 3, your program should return all 5 unique BST’s shown below.


   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""

from itertools import permutations

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
	# !!! this problem has not been solved
    # @param A : integer
    # @return a list of TreeNode 
    def generateTrees(self, A):
        res = []
        l = list(permutations(range(1, A+1)))
        for i in l:
            temp = None
            for j in i:
                temp = self.insert(temp, j)
            if res == []:
                res.append(temp)
            else:
                if not self.identicalTrees(temp,res[-1]):
                    res.append(temp)
        return res

    # Insert a node with value x to root A
    def insert(self, A, x):
        if A == None:
            A = TreeNode(x)
        elif x <= A.val:
            A.left = self.insert(A.left, x)
        else:
            A.right = self.insert(A.right, x)
        return A

    # Check if two trees are identical
    def identicalTrees(self, a, b):
        # 1. Both empty
        if a is None and b is None:
            return True
        # 2. Both non-empty -> Compare them
        if a is not None and b is not None:
            return ((a.val == b.val) and
                        self.identicalTrees(a.left, b.left) and
                        self.identicalTrees(a.right, b.right))


if __name__ == '__main__':

    s = Solution() # create Solution object

	A = 4
    r = s.generateTrees(A)
