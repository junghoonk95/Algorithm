n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()

ans = 0
for coin in coins:
    if coin <= k:
        ans += k//coin
        k %= coin
    if k == 0:
        break
print(ans)
