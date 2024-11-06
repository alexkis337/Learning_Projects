def romanToInt(s):
    int_num = 0
    replacer = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for elem in range(len(s)-1):
        if replacer[s[elem]] >= replacer[s[elem+1]]:
            int_num += replacer[s[elem]]
        else:
            int_num -= replacer[s[elem]]
    int_num += replacer[s[len(s)-1]]
    print(int_num)
    return int_num

romanToInt('XXL')