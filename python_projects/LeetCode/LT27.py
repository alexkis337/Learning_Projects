class Solution:
    def removeDuplicates(self, nums, val):
        elem = 0
        while (elem <len(nums)):
            if nums[elem] == val and nums[elem] != '_':
                nums.pop(elem)
                nums.append('_')
                elem -= 1
            elem += 1
        return int(len(nums) - nums.count('_'))


x = Solution()
print(x.removeDuplicates([3,2,2,3],3))