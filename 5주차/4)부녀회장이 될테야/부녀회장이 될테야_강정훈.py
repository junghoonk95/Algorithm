T=int(input())

for i in range(T):
    k=int(input()) #층
    n=int(input()) #호
    dp=[i for i in range(1,n+1)]
    for t in range(k):
        for i in range(1,n):
            dp[i]=dp[i-1]+dp[i]

    print(dp[-1])
