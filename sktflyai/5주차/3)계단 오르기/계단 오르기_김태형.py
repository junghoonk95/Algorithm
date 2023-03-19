N = int(input())
steps = []
for _ in range(N):
    steps.append(int(input()))
dp = [0 for _ in range(N)]
dp[0] = steps[0]
if N > 1:
    dp[1] = dp[0]+steps[1]

step_cnt = 0
for i in range(2,N):
    dp[i] = max(dp[i-2],dp[i-3]+steps[i-1]) + steps[i]

print(dp[-1])
