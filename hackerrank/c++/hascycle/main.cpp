#include <iostream>
#include <set>

using namespace std;
/* Has Cycle (linked list)
 *A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
 *
 * Complete the function provided in the editor below. It has one
 * parameter: a pointer to a Node object named that points to the head of
 * a linked list. Your function must return a boolean denoting whether or
 * not there is a cycle in the list. If there is a cycle, return true;
 * otherwise, return false.
 *
 */

struct Node {
    int data;
    struct Node* next;
} a, b, c;

bool HasCycle(Node* head){
    set <Node*> seen;
    Node* curr = head;
    while (curr != nullptr){
        if (const bool is_in = seen.find(curr) != seen.end()){
            return true;
        }
        seen.insert(curr);
        curr = curr->next; // use -> instead of . b/c curr is a pointer
    }
    return false;
}

int main() {

    a.data = 1;
    b.data = 2;
    c.data = 3;
    a.next = &b;
    b.next = &c;
    c.next = nullptr;

    std::cout << "The linked list contains a cycle: " << HasCycle(&a) << std::endl;
    return 0;
}