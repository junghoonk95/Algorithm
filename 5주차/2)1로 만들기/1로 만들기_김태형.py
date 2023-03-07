N = int(input())

dp = [0] * (10**6+2)

dp[0],dp[1],dp[2],dp[3] = 0,0,1,1

INF = 10**6+1
dp[10**6+1] = INF


for i in range(4,N+1):
    tmp1, tmp2, tmp3 = INF,INF,INF
    if i % 2 == 0:
        tmp2 = i // 2
    if i % 3 == 0:
        tmp3 = i // 3
    tmp1 = i-1
    dp[i] = min(dp[tmp1],dp[tmp2],dp[tmp3]) + 1

print(dp[N])
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# 0 1 1 1 2 3 2 3 3 2 3  4  3  4  4  4
