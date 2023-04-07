n= int(input())
dp=[0 for i in range(n+3)]

dp[0]=1
dp[1]=2
dp[2]=7
dp[3]=22
if n>3:
    for i in range(4,n+1):
        dp[i]=(dp[i-1]*2+dp[i-2]*3)% 1000000007
        for k in range(i - 3,-1,-1):
            dp[i]=(dp[i]+dp[k]*2)% 1000000007

print(dp[n])
