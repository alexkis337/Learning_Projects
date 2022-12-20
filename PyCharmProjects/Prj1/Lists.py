
#[[2, 1, 4], [4, 2, 8], [6, 3, 12]]
print([[x, int(x / 2), x * 2] for x in range(-6, 7, 2) if x > 0])