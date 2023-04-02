prices = [2,4,1]
best_buy = prices[0]
best_sell = 0
for x in range(1, len(prices)):
    if prices[x] < best_buy:
        best_buy = prices[x]
    elif prices[x] > best_sell:
        best_sell = prices[x]

print(best_sell-best_buy if best_sell-best_buy > 0 else 0)