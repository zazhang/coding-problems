#!usr/bin/env ipython

"""Coding interview problem (): 


"""

class Solution:
    def twoSum(self, nums, target):
        tmp = nums[:]
        for i in range(len(nums)):
            arg1 = target - nums[i]
            if self.bsearch(tmp, arg1) == True:
                index2 = nums.index(arg1) + 1
                index1 = i + 1
                if index1 < index2:
                    s = 'index1 = ' + str(index1) + ',' \
                        + 'index2 = ' + str(index2)
                    return s
                else:
                    s = 'index1 = ' + str(index2) + \
                        ',' + 'index2 = ' + str(index1)
                    return s

    def bsearch(self, lis, target):
        # binary search
        lis.sort()
        length = len(lis)
        if target > lis[length/2] and length/2 >= 1:
            new_lis = lis[length/2:]
            return self.bsearch(new_lis, target)
        elif target < lis[length/2] and length/2 >= 1:
            new_lis = lis[:length/2]
            return self.bsearch(new_lis, target)
        elif target == lis[length/2] and length/2 >= 1:
            return True
        else:
            return False
    # Binary search is too slow.
    # This implementation won't be able to avoid using same
    # number twice.

    # This implementation uses hash table/dictionary
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum2(self, nums, target):
        length = len(nums)
        table = dict()
        for j in range(length):
            diff = target - nums[j]
            if diff in table:
                return (table[diff] + 1, j + 1)
            table[nums[j]] = j  # assign values to the dict
    # We use harsh table (dict()) to search quickly (O(n)).
    # We swap the keys and values so that we can search for 'keys'
    # using values.
    # Values are inserted after search to avoid same number been
    # used twice.


if __name__ == "__main__":
    a = Solution()
    print a.twoSum([3, 2, 4], 6)
