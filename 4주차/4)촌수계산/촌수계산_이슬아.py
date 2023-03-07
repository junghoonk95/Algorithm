n=int(input())
start,end=map(int,input().split())
m=int(input())

graph=[[]for i in range(n+1)]
visited=[False]*(n+1)

answer=0

for i in range(m):
    parent,child=map(int,input().split())
    graph[parent].append(child)
    graph[child].append(parent)

for i in range(1,n+1):
  graph[i].sort()

result=-1
def dfs(graph,v,answer):
    visited[v]=True
    if v==end:
        result=answer
        print(answer)
        exit()
    for i in graph[v]:
        if visited[i]!=True:
            dfs(graph,i,answer+1)

dfs(graph,start,answer)

if result==-1:
    print(-1)
