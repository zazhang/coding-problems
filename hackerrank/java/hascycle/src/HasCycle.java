import java.util.HashSet;

/* Has Cycle (linked list)
A linked list is said to contain a cycle if any node is visited more than once while traversing the list.

Complete the function provided in the editor below. It has one parameter: a pointer to a Node object named that points to the head of a linked list. Your function must return a boolean denoting whether or not there is a cycle in the list. If there is a cycle, return true; otherwise, return false.
*/

public class HasCycle {

    static class Node {
        int data;
        Node next;
        Node(int d) {data = d; next = null;}
        }

    static boolean hasCycle(Node head) {
        Node curr = head;
        HashSet<Node> seen = new HashSet<Node>();
        while(curr != null){
            if (seen.contains(curr)){
                return true;
            }
            seen.add(curr);
            curr = curr.next;
        }
        return false;
    }

    public static void main(String[] args) {
        Node a  = new Node(1);
        Node b = new Node(2);
        Node c = new Node(1);
        a.next = b;
        b.next = c;
        c.next = a;

        boolean answer = hasCycle(a);
        System.out.println("The answer is " + answer);
    }
}


