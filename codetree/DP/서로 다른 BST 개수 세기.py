'''
BST란 자식을 2개 이하로 갖는 이진 탐색 트리입니다. 각 노드마다 왼쪽에 있는 모든 노드들의 값이 해당 노드의 값 보다 작아야 하고, 오른쪽에 있는 모든 노드들의 값이 해당 노드의 값 보다 커야 합니다.

1부터 N까지의 숫자들을 단 한 번씩만 써서 만들 수 있는 노드의 개수가 N인 서로 다른 이진 탐색 트리 개수를 세는 프로그램을 작성해보세요.
'''


N=int(input())

dp=[-1 for i in range(N+3)]

dp[0]=1
dp[1]=1
dp[2]=2
dp[3]=5

def funcdp(n):
    sol=0
    for i in range(n):
        sol=sol+dp[i]*dp[n-1-i]
    return sol
if N>=3:
    for i in range(4,N+1):
        dp[i]=funcdp(i)

print(dp[N])
