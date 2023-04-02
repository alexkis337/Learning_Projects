class Solution:
    def longestCommonPrefix(self, strs):
        strs = sorted(strs, key=len)  # sort by length
        result = strs[0]
        print(result)

        for word in range(len(strs)-1):
            print(strs[word])
            for letter in range(len(result)):
                print(letter)
                print(strs[word][letter], strs[word+1][letter])
                if strs[word][letter] != strs[word+1][letter]:
                    result = result[:letter]
                else:
                    result = result

        print(result)
        return result


x = Solution()
x.longestCommonPrefix(["cir","car"])
