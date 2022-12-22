class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        self.s = s

        vowels = ['a', 'e', 'i', 'o', 'u']
        print()
        half_1 = s[:int(len(s)/2)]
        half_2 = s[int(len(s)/2):]
        print(half_1)
        print(half_2)
        i = 0
        for elem in half_1:
            if elem.lower() in vowels:
                i += 1
        for elem in half_2:
            if elem.lower() in vowels:
                i -= 1
        if i == 0:
            return True
        else:
            return False

x = Solution()
print(x.halvesAreAlike('UO'))