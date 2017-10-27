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
# Binary search is two slow.
# This implementation won't be able to avoid using same
# number twice.

if __name__ == "__main__":
    a = Solution()
    print a.twoSum([3, 2, 4], 6)
