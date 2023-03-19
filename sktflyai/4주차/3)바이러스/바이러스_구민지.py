n=int(input())
v=int(input())

graph=[[] for _ in range(n+1)]

for _ in range(v):
    i,j = list(map(int,input().split()))
    graph[i].append(j)
    graph[j].append(i)
    graph[i].sort()
    
    
ans=[]
visited=[False]*(n+1)
def DFS(graph,v,visited):
    visited[v]=True
    ans.append(v)
    
    for i in graph[v]:
        if not visited[i]:
            DFS(graph,i,visited)
    
DFS(graph,1,visited)
print(len(ans)-1)
