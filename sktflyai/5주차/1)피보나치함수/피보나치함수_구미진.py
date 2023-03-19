T = int(input())

def fibo(n):
    for i in range(2, n+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

for i in range(T):
    N = int(input())
    dp = [[0, 0] for _ in range(50)] # 50x2 2차원 배열
    dp[0][0], dp[0][1], dp[1][0], dp[1][1] = 1, 0, 0, 1
    fibo(N)
    print(dp[N][0], dp[N][1])