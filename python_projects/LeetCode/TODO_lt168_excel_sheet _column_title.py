class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        lst = []
        result = ''
        while columnNumber > 0:
            letter = columnNumber % 26
            if letter == 0:
                result = chr(96 + 26) + result
            else:
                result = chr(96 + letter) + result
            columnNumber = columnNumber//26
        return result.upper()


x = Solution()
print(x.convertToTitle(456))


