class Solution:
    def climbStairs(self, n: int) -> int:
        lst = [1, 1]
        for elem in range(2, n+1):
            item = lst[elem-2]+lst[elem-1]
            lst.append(item)

        return lst[-1]


x = Solution()
print(x.climbStairs(6))
