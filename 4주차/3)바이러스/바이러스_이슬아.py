from collections import deque
n=int(input())
m=int(input())
graph=[[]for i in range(n+1)]

for i in range(m):
  start,end=map(int,input().split())
  graph[start].append(end)
  graph[end].append(start)

for i in range(1,n+1):
  graph[i].sort()
  #간선 정보에 따라 정렬

visited=[False]*(n+1)
count=0
def dfs(graph,v,visited):
    global count
    visited[v]=True
    count=count+1
    for i in graph[v]:
        if visited[i]!=True:
            dfs(graph,i,visited)
            
dfs(graph,1,visited)
print(count-1)
