n = int(input())
times = list(map(int, input().split()))

times.sort()

ans = 0
for i in range(n):
    ans += times[i] * (n-i)

print(ans)
