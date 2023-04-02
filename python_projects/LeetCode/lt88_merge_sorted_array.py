class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1, p2 = m-1, n-1
        for right in range(m+n-1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[right] = nums1[p1]
                p1 -= 1
            else:
                nums1[right] = nums2[p2]
                p2 -= 1

        return nums1

x = Solution()
print(x.merge(nums1 = [0], m = 0, nums2 = [1], n = 1))
