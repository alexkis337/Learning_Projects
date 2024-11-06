def cantor(n : int) -> str:
    if n == 1:
        return 1/1
    if n == 2:
        return 1/2
    if n == 3:
        return 2/1


    triang = 1
    while (triang * (triang + 1) / 2) < n:
        triang += 1

    print(triang)
    # print('triang', triang)
    # print('pos', i)
    print(7 % 2)

    if triang % 2 == 1:
        print(triang // 2 == 1)
        i = int(triang * (triang - 1) / 2) + 1
        print('start pos', i)
        print('triang', triang)
        num = triang
        denum = 1
        while i != n:
            print(f'{num}/{denum}', ' pos', i)
            num -= 1
            denum += 1
            i += 1

    else:
        i = int(triang * (triang - 1) / 2) + 1
        print('start pos', i)
        print('triang', triang)
        num = 1
        denum = triang
        while i < n:
            print(f'{num}/{denum}', ' pos', i)
            num += 1
            denum -= 1
            i += 1

    return f'{num}/{denum}'

print('final', cantor(22))