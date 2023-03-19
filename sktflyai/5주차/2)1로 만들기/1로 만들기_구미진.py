N = int(input())

d = [0] * (N+3)
d[2], d[3] = 1, 1

for i in range(4, N+1):
    if i % 2 == 0 and i % 3 == 0:
        d[i] = 1 + min(d[i//3], d[i//2], d[i-1])
    elif i % 3 == 0:
        d[i] = 1 + min(d[i//3], d[i-1])
    elif i % 2 == 0:
        d[i] = 1 + min(d[i//2], d[i-1])
    else:
        d[i] = 1 + d[i-1]

print(d[N])

'''
1. 예제 관찰하면서 점화식 표현 
if i % 3 == 0:
    d[i] = 1 + min(d[i//3], d[i-1])

2. 반복문 돌면서 dp 테이블 업데이트하기
'''