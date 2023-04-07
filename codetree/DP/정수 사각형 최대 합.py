'''
N×N 행렬이 주어졌을 때, (1,1)에서 시작하여 오른쪽 혹은 밑으로만 이동하여 (N,N)으로 간다고 했을 때 거쳐간 위치에 적혀있는 숫자의 합을 최대로 하는 프로그램을 작성해보세요.
'''

N=int(input())

arr=[list(map(int,input().split())) for i in range(N)]

dp=[[0 for _ in range(N)] for _ in range(N)]
dp[0][0]=arr[0][0]
for i in range(1,N):
    dp[0][i]=dp[0][i-1]+arr[0][i]

for j in range(0,N-1):
    dp[j+1][0]=dp[j][0]+arr[j+1][0]


for i in range(1,N):
    for j in range(1,N):
        if dp[i][j]==0:
            dp[i][j]=max(dp[i-1][j]+arr[i][j],dp[i][j-1]+arr[i][j])

print(dp[N-1][N-1])

