T = int(input())

# 1. dp 테이블 세팅 - dp 값은 각 호에 사는 사람들 수 합
def dynamic(k, n):
    dp = [[0] * n for _ in range(k+1)] # k x n 2차원 배열로 선언
    
    # dp 테이블 초기화
    dp[0] = [i for i in range(1, n+1)]
    for i in range(k+1):
        dp[i][0] = 1

    # 2. 점화식으로 표현
    for i in range(1, k+1):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[k][n-1]      

for i in range(T):
    k, n = int(input()), int(input())
    print(dynamic(k, n)) # k층 n호