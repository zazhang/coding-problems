#!usr/bin/env ipython

"""Coding interview problem (trees): 

Given a BST node, return the node which has value just greater than the given node.

Example:

Given the tree

               100
              /   \
            98    102
           /  \
         96    99
          \
           97
Given `97`, you should return the node corresponding to `98` as thats the value just greater than `97` in the tree.
If there are no successor in the tree ( the value is the largest in the tree, return `NULL`).

Using recursion is not allowed.

Assume that the value is always present in the tree.

"""

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None    

    def insert(self, A, x):
        if A == None:
            A = TreeNode(x)
        elif x <= A.val:
            A.left = self.insert(A.left, x)
        else:
            A.right = self.insert(A.right, x)
        return A


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        current = self.find(A,B)
        #print current.val
        if current == None: return None

        # case 1: has right subtree,
        # successor is the leftmost node on right subtree
        if current.right != None:
            if A == None: return None
            else: current = current.right
            while current.left != None:
                current = current.left
            return current
        else: # case 2: no right subtree
            successor = None
            ancestor = A
            #print ancestor.val
            while ancestor != current:
                # if current is on left subtree of ancestor
                if current.val <= ancestor.val: 
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
        return successor

    # This is a recursion implementation of finding a node given value
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def find(self, A, B):
        if A == None: return None
        elif A.val == B: return A
        elif A.val < B: return self.find(A.right, B)
        else: return self.find(A.left, B)

    # This implementation uses loop instead of recursion
    def find2(self, A, B):
        if A == None: return None
        while A != None:                
            if A.val == B: return A
            elif A.val < B:
                A = A.right
            else:
                A = A.left

    # This is the answer implementation
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor2(self, A, B):
        root = A
        succ = root
        while root.val != B:
            if B < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        if root.right != None:
            root = root.right
            while root.left!=None:
                    root = root.left
            return root
        else:
            if succ.val <= B:
                return None
            else:
                return succ                


if __name__ == '__main__':

    s = Solution() # create Solution object

    A = TreeNode(31)
    lis = [19, 34, 13, 25, -1, 97, 7, 16, 22, 28, 64, 112, 4, 10, -1, -1, -1, -1, -1, -1, 37, 67, 100, 13, 1, -1, -1, -1, -1, 52, -1, 73, -1, 106, 124, 175, -1, -1, 46, 61, 70, 79, 103, 109, 121, 145, 169, 220, 43, 49, 55, -1, -1, -1, 76, 88, -1, -1, -1, -1, 115, -1, 139, 151, 166, 172, 181, 226, 40, -1, -1, -1, -1, 58, -1, -1, 85, 94, -1, 118, 133, 142, 148, 157, 163, -1, -1, -1, 178, 205, 223, -1, -1, -1, -1, -1, 82, -1, 91, -1, -1, -1, 127, 136, -1, -1, -1, -1, 154, -1, -1, -1, -1, -1, 193, 211, -1, -1, -1, -1, -1, -1, -1, 130, -1, -1, -1, -1, 190, 202, 208, 214, -1, -1, 187, -1, 196, -1, -1, -1, -1, 217, 184, -1, -1, 199, -1, -1, -1, -1, -1, -1]
    lis = filter(lambda a: a != -1, lis)
    for i in lis:
        A.insert(A, i)
    B = 13
    print s.getSuccessor(A,B).val
