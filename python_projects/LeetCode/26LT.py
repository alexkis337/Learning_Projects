class Solution:
    def removeDuplicates(self, nums):
        elem = 0
        while (elem <len(nums)-1):
            if nums[elem] == nums[elem+1] and nums[elem] != '_':
                nums.pop(elem+1)
                nums.append('_')
                elem -= 1
            elem += 1
        return nums


x = Solution()
print(x.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))