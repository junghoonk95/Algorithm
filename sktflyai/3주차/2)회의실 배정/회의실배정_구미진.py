import sys
input = sys.stdin.readline
n = int(input())

li = [0 for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    li[i] = (a, b)

li.sort(key=lambda x : (x[0], x[1]))

cnt = 0
meet = (0, 0)
for i in range(n):
    if li[i][0] >= meet[1]:
        meet = li[i]
        cnt += 1
    if li[i][1] < meet[1]: #바꾸기니깐 cnt X
        meet = li[i]

print(cnt)