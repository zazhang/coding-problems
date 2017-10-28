#!usr/bin/env ipython

"""Coding interview problem (): 


"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def getData(self):
        return self.val

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.val = newdata

    def setNext(self, newnext):
        self.next = newnext


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = ListNode(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node

    def remove(self, node_val):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.val == node_val:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
            previous_node = current_node
            current_node = current_node.next


class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        result = l1
        residue = (l1.val + l2.val) / 10
        l1.val = (l1.val + l2.val) % 10
        while l1.next is not None and l2.next is not None:
            l1.next.val = residue + l1.next.val + l2.next.val
            residue = l1.next.val / 10
            l1.next.val = l1.next.val % 10
            l1 = l1.next
            l2 = l2.next
        if l1.next is None:
            l1.next = l2.next
        while l1.next is not None:
            l1.next.val += residue
            residue = l1.next.val / 10
            l1.next.val = l1.next.val % 10
            l1 = l1.next
        if residue > 0:
            l1.next = ListNode(residue)
        return result

    # This implementation uses newly defined helper functions
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers2(self, l1, l2):
        results = []
        while l1.head is not None:
            n = l1.head.getData()
            m = l2.head.getData()
            sum_val = n + m
            l1.remove(n)
            l2.remove(m)
            results.append(sum_val)
        for i in range(len(results)):
            if results[i] != results[-1]:
                if results[i] == 10:
                    results[i] = 0
                    results[i+1] = results[i+1] + 1
            else:
                if results[-1] == 10:
                    results[-1] = 0
                    results.append(1)
        return results


if __name__ == "__main__":
    l3 = ListNode(5)
    l4 = ListNode(5)

    l1 = LinkedList()
    l1.append(2)
    l1.append(4)
    l1.append(3)
    l1.append(5)
    l2 = LinkedList()
    l2.append(5)
    l2.append(6)
    l2.append(4)
    l2.append(1)

    a = Solution()
    print a.addTwoNumbers(l1, l2)
