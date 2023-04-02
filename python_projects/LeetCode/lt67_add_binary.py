class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

x = Solution()
print(x.addBinary('1010', '1011'))
