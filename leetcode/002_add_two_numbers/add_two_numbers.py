# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


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


# create ListNode class for test purpose
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == "__main__":
    l1 = ListNode(5)
    l2 = ListNode(5)
    a = Solution()
    print a.addTwoNumbers(l1, l2)
