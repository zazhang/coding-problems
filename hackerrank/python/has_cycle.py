#!usr/bin/env ipython

""" Detect cycle (linked list)

A linked list is said to contain a cycle if any node is visited more than
once while traversing the list.
Complete the function provided in the editor below. 
It has one parameter: a pointer to a Node object named that points to 
the head of a linked list. Your function must return a boolean denoting
whether or not there is a cycle in the list. 
If there is a cycle, return true; otherwise, return false.

TODO: need revise traverse and has_cycle2, a linked list with a cycle means 
a node points to another node, not means two nodes have the same data.
"""

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

def has_cycle(head):
    curr = head
    seen = set()
    while curr:
        if curr in seen:
            return True
        seen.add(curr)
        curr = curr.next
    return False
    
    
if __name__ == '__main__':

    a = Node(1)
    b = Node(2)
    c = Node(1)
    a.next = b
    b.next = c
    c.next = a
    answer = has_cycle(a)
    print answer
