N=int(input())
arr=[]
dp=[0 for i in range(N)]
for i in range(N):
    arr.append(int(input()))
arr.reverse()

if N==1:
    print(arr[0])
elif N==2:
    print(arr[0]+arr[1])
else:

    dp[0]=arr[0]
    dp[1]=arr[0]+arr[1]
    dp[2]=arr[0]+arr[2]

    for i in range(3,N):
        dp[i]=max(arr[i-1]+arr[i]+dp[i-3],dp[i-2]+arr[i])

    print(max(dp[-2], dp[-1]))
