n = int(input())
time = sorted([tuple(map(int, input().split())) for _ in range(n)])
              
time.sort()
time.sort(key = lambda x: x[1])
ans = end = 0
for s, e in time:
    if s >= end:
        ans += 1
        end = e
print(ans)
