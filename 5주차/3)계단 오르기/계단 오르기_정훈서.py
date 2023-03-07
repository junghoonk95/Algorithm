n = int(input())
steps = [int(input()) for _ in range(n)]

dp=[0]*(n) # dp 리스트
if len(steps) <= 2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(steps))
else: # 계단이 3개 이상일 때
    dp[0] = steps[0] # 1번째 계단
    dp[1] = steps[0] + steps[1] # 2번째 계단
    for i in range(2, n): # 3번째 계단부터 dp 점화식 이용해서 최대값 구하기
        dp[i] = max(dp[i-3] + steps[i-1] + steps[i], dp[i-2] + steps[i])
        # i=2 - max(1+step[1]+step[2], dp[0]+step[2]) : 2, 3번째 계단 vs 1, 3번째 계단
        # i=3 - max(2번째 계단+step[2]+step[3], dp[1]+step[3]) : 1, 3, 4계단 vs 1, 2, 4번째 계단
        # i=4 - max(1,2번째 계단+step[3]+step[4], dp[2]+step[4]) : 1, 2, 4, 5 vs ~ 3, 5
        # ...
    print(dp[-1]) # 점화식에 step[i]가 더해지기에 마지막 계단 포함

'''
dp[i-3]+s[i-1]+s[i] : i-3까지의 계단 점수 최댓값과 i-1, i 계단의 합.
dp[i-2]+s[i] : i-2까지의 계단 점수 최댓값과 i 계단의 합.
'''