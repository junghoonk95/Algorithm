from collections import deque
n,m,v=map(int,input().split())
graph=[[]for i in range(n+1)]

for i in range(m):
  start,end=map(int,input().split())
  graph[start].append(end)
  graph[end].append(start)

for i in range(1,n+1):
  graph[i].sort()
  #간선 정보에 따라 정렬

visited=[False]*(n+1)

def dfs(graph,v,visited):
  visited[v]=True
  print(v,end=' ')
  for i in graph[v]:
    if visited[i]!=True:
      dfs(graph,i,visited)


def bfs(graph,v,visited):
  dq=deque()
  dq.append(v)
  visited[v]=True
  while dq:
    a=dq.popleft()
    print(a,end=' ')
    for i in graph[a]:
        if visited[i]!=True:
          dq.append(i)
          visited[i]=True

dfs(graph,v,visited)
visited=[False]*(n+1)
print('')
bfs(graph,v,visited)
