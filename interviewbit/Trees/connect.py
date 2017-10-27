#!usr/bin/env ipython

"""Coding interview problem (trees): 

See `https://www.interviewbit.com/problems/next-pointer-binary-tree/`

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:
You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

Example :

Given the following perfect binary tree,

         1
       /  \
      2    5
     / \  / \
    3  4  6  7
After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 5 -> NULL
     / \  / \
    3->4->6->7 -> NULL
Note that using recursion has memory overhead and does not qualify for constant space.

My notes:
- find the distance to root
- nodes with the same distance are at the same level, where leftmost has the smallest value
- use a find() to locate a node
- connect nodes at the same level, from smallest to largest, largest to `None`
"""

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def insert(self, A, x):
        if A == None:
            A = TreeNode(x)
        elif x <= A.val:
            A.left = self.insert(A.left, x)
        else:
            A.right = self.insert(A.right, x)
        return A


class Solution:
	# !!! this problem has not been solved
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        parent = None
        if root == None: return
            
        root.next = None
            while root.left != None:
                self.setNext(root)
                parent = root
                root = root.left
            while root.right != None:

    # not useful maybe
    def setNext(self, root, parent):
        if root == None: return root
            
        if root.left != None and root.right != None:
            root.left.next = root.right
            root.right.next = None
        elif root.left != None and root.right == None:
            root.left.next = None
        elif root.left == None and root.right != None:
            root.right.next = None
        return root

    # Find a node given value
    # @param A : root node of tree
    # @param B : integer    
    def find(self, A, B):
        if A == None: return None
        while A != None:                
            if A.val == B: return A
            elif A.val < B:
                A = A.right
            else:
                A = A.left


if __name__ == '__main__':

    s = Solution() # create Solution object

    A = TreeNode(31)
    lis = [19, 34, 13, 25, -1, 97, 7, 16, 22, 28, 64, 112, 4, 10, -1, -1, -1, -1, -1, -1, 37, 67, 100, 13, 1, -1, -1, -1, -1, 52, -1, 73, -1, 106, 124, 175, -1, -1, 46, 61, 70, 79, 103, 109, 121, 145, 169, 220, 43, 49, 55, -1, -1, -1, 76, 88, -1, -1, -1, -1, 115, -1, 139, 151, 166, 172, 181, 226, 40, -1, -1, -1, -1, 58, -1, -1, 85, 94, -1, 118, 133, 142, 148, 157, 163, -1, -1, -1, 178, 205, 223, -1, -1, -1, -1, -1, 82, -1, 91, -1, -1, -1, 127, 136, -1, -1, -1, -1, 154, -1, -1, -1, -1, -1, 193, 211, -1, -1, -1, -1, -1, -1, -1, 130, -1, -1, -1, -1, 190, 202, 208, 214, -1, -1, 187, -1, 196, -1, -1, -1, -1, 217, 184, -1, -1, 199, -1, -1, -1, -1, -1, -1]
    lis = filter(lambda a: a != -1, lis)
    for i in lis:
        A.insert(A, i)
    print s.connect(A)
