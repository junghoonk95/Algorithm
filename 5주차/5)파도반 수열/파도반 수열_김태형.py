'''
1 1 1 2 2 3 4 5 7 9 12 

4번째부터 dp[i] = dp[i-3] + dp[i-2]
'''
dp = [0 for _ in range(101)]
dp[0],dp[1],dp[2] = 1,1,1

for i in range(3,101):
    dp[i] = dp[i-3] + dp[i-2]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N-1])