import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    dp = [[]]*41

    dp[0] = [1, 0]
    dp[1] = [0, 1]
    dp[2] = [1, 1]

    for i in range(3, N+1):
        dp[i] = [dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]]
    print(dp[N][0], dp[N][1])

# 시간 초과
def fib(n):
global cnt_0
global cnt_1
if n == 0:
    cnt_0 += 1
    return 0
elif n == 1:
    cnt_1 += 1
    return 1
else:
    return fib(n-1) + fib(n-2)

T = int(input())

for _ in range(T):
    cnt_0 = 0
    cnt_1 = 0
    N = int(input())
    fib(N)
    print(cnt_0, cnt_1)
