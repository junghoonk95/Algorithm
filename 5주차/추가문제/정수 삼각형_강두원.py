def solution(triangle):
    answer = 0
    dp = [[0] * (i+1) for i in range(len(triangle))]
    for i, line in enumerate(triangle):
        if i == 0:
            dp[0][0] = triangle[0][0]
            continue
        for j, e in enumerate(line):
            if j == 0:
                dp[i][j] = dp[i-1][j] + e
            elif j == len(line) - 1:
                dp[i][j] = dp[i-1][j-1] + e
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + e
    
    answer = max(dp[-1])
    return answer

'''
      7
    10 15
  18 16 15
 20 25 20 19
24 30 27 26 24
'''
