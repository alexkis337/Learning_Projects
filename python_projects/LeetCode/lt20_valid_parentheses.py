class Solution:
    def isValid(s):
        didi = {'(': ')', '[': ']', '{': '}'}
        checker = []
        for elem in s:
            if len(s) < 2:
                return False
            elif elem in ('(', '[', '{'):
                checker.append(elem)
            elif (len(checker) > 0) and (elem == didi[checker[-1]]):
                checker = checker[:-1]
            else:
                return False
        return checker == []

