#!usr/bin/env ipython

""" Is it a BST (binary search tree)
For the purposes of this challenge, we define a binary search tree 
to be a binary tree with the following ordering properties:

The  value of every node in a node's left subtree is less than 
the data value of that node.
The  value of every node in a node's right subtree is greater 
than the data value of that node.
Given the root node of a binary tree, 
can you determine if it's also a binary search tree?

Complete the function in your editor below, 
which has 1 parameter: a pointer to the root of a binary tree. 
It must return a boolean denoting whether or not the binary tree
is a binary search tree. You may have to write one or more 
helper functions to complete this challenge.

"""

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkBST(root):
    if root:
        left = root.left
        right = root.right
        if left.data >= right.data:
            return 0
        traverse(root.left)            
        traverse(root.right)
        return 1


if __name__ == '__main__':

    a = node(1)
    b = node(2)
    c = node(3)
    d = node(4)
    e = node(5)
    a.left = b
    b.left = c
    a.right = d
    d.left = e
    answer = checkBST(a)
    print answer

