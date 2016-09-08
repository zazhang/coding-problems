class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
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
