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

Note: this implementation uses heapsort() and is slow, didn't pass LC tests.

"""


class MedianFinder(object):
    def __init__(self):
        """
        create a heap to store data
        """
        self.heap = []

    def maxHeapify(self, arr, n, i):
        """
        :type arr: a list of float
        :type n: int
        :type i: int
        :rtype: void
        """        
        largest = i # Initialize largest as root
        l = 2 * i + 1 # left = 2*i + 1
        r = 2 * i + 2 # right = 2*i + 2
    
        # See if left child of root exists and is
        # greater than root
        if l < n and arr[i] < arr[l]:
            largest = l
    
        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r
    
        # Change root, if needed
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i] # swap
    
            # Heapify the root.
            self.maxHeapify(arr, n, largest)

    def minHeapify(self, arr, n, i):
        """
        :type arr: a list of float
        :type n: int
        :type i: int
        :rtype: void
        """        
        smallest = i # Initialize largest as root
        l = 2 * i + 1 # left = 2*i + 1
        r = 2 * i + 2 # right = 2*i + 2
    
        # See if left child of root exists and is
        # smaller than root
        if l < n and arr[i] > arr[l]:
            smallest = l
    
        # See if right child of root exists and is
        # smaller than root
        if r < n and arr[smallest] > arr[r]:
            smallest = r
    
        # Change root, if needed
        if smallest != i:
            arr[i],arr[smallest] = arr[smallest],arr[i] # swap
    
            # Heapify the root.
            self.minHeapify(arr, n, smallest)            

    # The main function to sort an array of given size
    def heapSort(self, arr, algo = 'max'):
        n = len(arr)
    
        # Build a maxheap.
        for i in range(n, -1, -1):
            if algo == 'min':
                self.minHeapify(arr, n, i)
            else:
                self.maxHeapify(arr, n, i)
    
        # One by one extract elements
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i] # swap
            if algo == 'min':
                self.minHeapify(arr, i, 0)
            else:
                self.maxHeapify(arr, i, 0)
        self.heap = arr
        return self.heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.heap.append(num)

    def findMedian(self):
        """
        :rtype: float
        """
        self.heap = self.heapSort(self.heap)
        n = len(self.heap)
        ind = n // 2
        if n % 2 == 0:
            median = (self.heap[ind] + self.heap[ind-1]) / 2.0
        else:
            median = self.heap[ind]
        return float(median)

        
if __name__ == '__main__':

    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(4)
    obj.addNum(2)
    obj.addNum(5)
    obj.addNum(3)
    param_2 = obj.findMedian()
    print param_2
