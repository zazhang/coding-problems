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

public class CheckBST {

    static class Node {
        int data;
        Node left;
        Node right;
        Node (int d){data =d; left = null; right = null;}
    }

    static boolean check(Node root, int[] prev){
        // Note: declaring `prev` as an array instead of int makes `prev` an
        // object, which can be passed by reference.
        boolean result = true;
        if (root.left != null) {
            result = result && check(root.left, prev);
        }
        //System.out.println("before: "+ prev[0]);
        if (prev[0] >= root.data){
            return false;
        }
        prev[0] = root.data;
        //System.out.println("after: "+ prev[0]);
        if (root.right != null){
            result = result && check(root.right, prev);
        }
        return result;
    }

    static boolean checkBST(Node root) {
        int[] prev = {-1};
        return check(root, prev);
    }

    public static void main(String[] args){
        Node a = new Node(1);
        Node b = new Node(2);
        Node c = new Node(3);
        Node d = new Node(4);
        Node e = new Node(5);
        Node f = new Node(5);
        Node g = new Node(7);
        d.left =b;
        d.right = f;
        b.left = a;
        b.right = c;
        f.left = e;
        f.right = g;
        boolean answer = checkBST(d);
        System.out.println("This binary tree is a BST: " + answer);
    }
}
