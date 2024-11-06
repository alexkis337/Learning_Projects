class Solution:
    def twoSum(self, nums, target):
        hashMap = {nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            if target-nums[i] in hashMap and hashMap[target-nums[i]] != i:
                return i, hashMap[target-nums[i]]


x = Solution()
xx = x.twoSum([3,2,4 ], 6)
yy = x.twoSum([3,3], 6)
print(xx)
print(yy)

# this is from two sum