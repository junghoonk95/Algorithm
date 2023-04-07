n=int(input())

dp=[-1 for i in range(n+2)]

dp[0]=1
dp[1]=0
dp[2]=1
dp[3]=1


if n>=4:
    for i in range(4,n+1):
        dp[i]=(dp[i-2]+dp[i-3]) %10007
print(dp[n])
