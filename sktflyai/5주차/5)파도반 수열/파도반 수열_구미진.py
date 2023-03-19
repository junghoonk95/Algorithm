T = int(input())

def dynamic(N):
    dp = [1, 1, 1, 2, 2, 3, 4, 5]
    if N > 8:
        dp.extend([0] * (N-8))
        for i in range(8, N):
            dp[i] = dp[i-1] + dp[i-5]
    return dp[N-1]

for i in range(T):
    N = int(input())
    print(dynamic(N))

'''
0 1 2 3 4 5      6      7      8      9      10
1 1 1 2 2 3(2+4) 4(1+5) 5(0+6) 7(3+7) 9(4+8) 12(5+9)
'''