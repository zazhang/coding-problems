#!usr/bin/env ipython

"""Find Median from Data Stream (LC295)

Median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value. 
So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.

"""


import heapq

class MedianFinder(object):
    """
    This problem can be solved using maxHeap and minHeap.
    Initialize the data structure as a maxHeap and a minHeap.
    Add a number to the data structure in two steps
        First, if `num < current_median`, push to maxHeap, else, push to
            minHeap
        Second, check the length of two heaps, if equal, the result_median
            is the average of roots of both heaps
        Third, if length of two heaps are not equal, the root of the larger
            one is the result_median.
    heapq package implements minHeap, a maxHeap can be obtained using 
        `num * -1`
    """
    def __init__(self):
        """
        create a heap to store data
        """
        self.minheap = []
        self.maxheap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if not self.minheap or num>self.minheap[0]:
            heapq.heappush(self.minheap, num)
        elif not self.maxheap or num<-self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            if len(self.minheap)>len(self.maxheap)+1:
                heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.minheap, num)
        
        # now make it balanced
        while len(self.minheap)>len(self.maxheap)+1:
            item = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -item)
            
        while len(self.maxheap)>len(self.minheap):
            item = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -item)
            
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if not self.maxheap and not self.minheap:
            return None
        if len(self.maxheap)==len(self.minheap):
            return (self.minheap[0]-self.maxheap[0])*1.0/2
        else:
            return float(self.minheap[0])

        
if __name__ == '__main__':

    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(4)
    obj.addNum(2)
    obj.addNum(5)
    obj.addNum(3)
    param_2 = obj.findMedian()
    print param_2

