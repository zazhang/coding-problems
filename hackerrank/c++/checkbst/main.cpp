#include <iostream>

/* Is it a BST (binary search tree)
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

Idea: inorder traversal goes like this: left, root, right, hence, we 
can check if ith element is greater than (i-1)th element, if not, it is
not a BST.

Test cases:
Input:
2
1 2 3 5 4 6 7
Output:
No (b/c 4 smaller than 5, but on its right sub-tree)

Input:
4
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 17 16 18 19 20 21 22 23 24 25 26 27 28 29 30 31
Output:
No

*/

struct Node {
    int data;
    Node* left;
    Node* right;
} a, b, c, d, e, f, g;

bool check(Node* root, int* prev){
    bool result = true;
    if (root->left != nullptr){
        result &= check(root->left, prev);
    }
    //std::cout << "before: " << prev << std::endl;
    if (*prev >= root->data){
        result &= false;
    }
    *prev = root->data;
    //std::cout << "after: " << prev << std::endl;
    if (root->right != nullptr){
        result &= check(root->right, prev);
    }

    return result;
}

bool checkBST(Node* root){
    int prev = -1;
    return check(root, &prev);
}

int main() {
    a.data = 3;
    a.left = &b;
    a.right = &c;
    b.data = 2;
    c.data = 6;
    b.left = &e;
    b.right = &f;
    e.data = 1;
    f.data = 4;
    c.left = &d;
    c.right = &g;
    d.data = 5;
    g.data = 7;

    std::cout << "This binary is a BST " << checkBST(&a) << std::endl;
}