arr = [1,2,3,4]
k = 2
max_len = arr[-1] + k
i = 0
for _ in range(1, max_len+1):
    if _ not in arr:
        i += 1
        if i == k:
            print(_)
            break


