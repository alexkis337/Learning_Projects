class Solution:
    def twoSum(self, nums: list, target: int):
        for elem in range(len(nums)):
            diff = target - nums[elem]
            if diff in nums[elem+1:]:
                print(elem, nums[elem+1:].index(diff)+len(nums[:elem+1]))
                return elem, nums[elem+1:].index(diff)+len(nums[:elem+1])


x = Solution()
xx = x.twoSum([3,2,4 ], 6)
yy = x.twoSum([3,3], 6)
print(xx)
print(yy)
