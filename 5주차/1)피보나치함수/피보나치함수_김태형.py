T = int(input())
dp = [0 for _ in range(41)]
# 0 1 2 3 4 5
# 0 1 1 2 3 5
dp[0],dp[1] = 0,1

# initialize
cnt_0,cnt_1 = 0,0
dp = [0 for _ in range(41)]
# 0 1 2 3 4 5
# 0 1 1 2 3 5
dp[0],dp[1] = 0,1

def fibonacci(N):
    global cnt_0,cnt_1
    if N == 0:
        cnt_0 += 1
        return dp[0]
    elif N == 1:
        cnt_1 += 1
        return dp[1]
    else:
        if dp[N]:
            return dp[N]
        else:
            dp[N] = fibonacci(N-1) + fibonacci(N-2)
            return dp[N]

fibonacci(40)

for _ in range(T):
    N = int(input())
    print(1 if N == 0 else dp[N-1],dp[N])