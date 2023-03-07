# https://maktubi.tistory.com/267

N = int(input())
sc = [int(input()) for _ in range(N)]
dp = [0] * N

if N < 2:
    dp[N-1] = sum(sc)
else:
    dp[0] = sc[0]
    dp[1] = dp[0] + sc[1]

for i in range(2, N):
    dp[i] = max(dp[i-2], dp[i-3] + sc[i-1]) + sc[i]

print(dp[N-1])

'''
- 마지막 계단은 반드시 포함
- 세 개가 연속되면 안됨
- 계단 사이는 하나만 건너뛸 수 있음

1. dp 테이블 세팅
dp 값은 해당 계단에서 얻을 수 있는 총 점수의 최댓값

2. 점화식 세우기
dp[i] = max(dp[i-2] + sc[i], dp[i-1] + sc[i])

3. 반복문 돌면서 dp 테이블 업데이트
'''
