class Solution:
    def isPalindrome(self, x: int) -> bool:

        return str(x) == str(x)[::-1]

x = Solution()
xx = x.isPalindrome(-121)
print(xx)