N,K = map(int,input().split())
W = [0]
V = [0]
for i in range(N):
    w,v = map(int,input().split())
    W.append(w)
    V.append(v)

# dp[i][j] : 처음부터 i번째까지 물건에 대해 용량 j였을 때 가치합의 최대값
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

# for _ in dp:
    # print(_)
for i in range(N+1):
    for j in range(K+1):
        if j>=W[i]:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-W[i]]+V[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])