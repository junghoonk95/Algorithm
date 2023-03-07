"""
solution(2) = 1
solution(3) = 1
solution(4) = 4 -> 2 -> 1 = 2
solution(5) = 5 -> 4 -> 2 -> 1 = 3
solution(6) = 6 -> 2 -> 1 = 2
solution(7) = 7 -> 6 -> 2 -> 1 = 3
solution(8) = 8 -> 4 -> 2 -> 1 = 3
solution(9) = 9 -> 3 -> 1 = 2
solution(10) = 10 -> 9 -> 3 -> 1 = 3
"""

import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1) # index를 1부터 사용

dp[0] = 0
dp[1] = 0 # 문제가 1을 만드는 것이므로, 이미 1이기 때문에 연산 횟수 0

for i in range(2, N+1):
    # 1을 뺀다.
    dp[i] = dp[i-1] + 1
    # X가 2로 나누어 떨어지면, 2로 나눈다.
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # X가 3으로 나누어 떨어지면, 3으로 나눈다.
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
print(dp[N])
print(dp)
