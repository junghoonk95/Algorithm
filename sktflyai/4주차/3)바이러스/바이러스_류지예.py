n = int(input())
line = int(input())
com = [[] * n  for _ in range(n+1)]
for _ in range(line):
  a, b = map(int, input().split())
  com[a].append(b)
  com[b].append(a)

cnt = 0
visited = [0] * (n+1)
def dfs(start):
  global cnt
  visited[start] = 1
  for i in com[start]:
    if visited[i] == 0:
      dfs(i)
      cnt +=1
 
dfs(1)
print(cnt)
