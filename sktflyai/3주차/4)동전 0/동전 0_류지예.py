n, k = map(int, input().split())

coin_list = []
for _ in range(n):
  coin = int(input())
  if coin <= k:
    coin_list.append(coin)

i = -1
cnt = 0
while k != 0:
  cnt += (k // coin_list[i])
  k %= coin_list[i]
  i -= 1

print(cnt)
