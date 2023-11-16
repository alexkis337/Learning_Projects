def sqrt(x):
    guess = x / 2
    while abs(guess * guess - x) > 0.1:
        guess = (guess + x / guess) / 2

    return round(guess//1)


result = sqrt(8)
print(result)
