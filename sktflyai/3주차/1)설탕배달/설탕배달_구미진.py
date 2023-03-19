n = int(input())
ans = []

for i in range(n//5 + 1):
    if (n - 5*i) % 3 == 0:
        cnt = i + (n - 5*i) // 3
        ans.append(cnt)

if ans:
    print(min(ans))
else:
    print(-1)

'''
5x + 3y = n에서 y의 최대 개수 구하는 문제
y = (n - 5x) / 3
y가 3으로 나누어 떨어지는지를 기준으로 경우 나누기
'''