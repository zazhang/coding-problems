class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        list1 = sorted(nums1)
        list2 = sorted(nums2)
        print list1
        print list2
        tmplist = list1 + list2
        print tmplist
        list3 = sorted(tmplist)
        length = len(list3)
        if length % 2 == 0:  # even
            result = float((list3[length/2] + list3[length/2-1]) / 2.0)
            return result
        elif length % 2 == 1:  # odd
            result = float(list3[length/2])
            return result

if __name__ == "__main__":
    a = Solution()
    print a.findMedianSortedArrays([], [6, 7])
