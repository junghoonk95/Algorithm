n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)
cnt = 0
for i in coins:
    if k == 0:
        break
    if k % i == k:
        continue
    cnt += k // i # 코인 갯수 증가
    k = k % i # 목표 금액 
print(cnt)
