N = int(input())
M = int(input())
graph = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0 for _ in range(N)]
visited[0] = 1
answer = 0

def dfs(now):
    global answer
    for node in graph[now]:
        if not visited[node]:
            visited[node] = 1
            answer += 1
            dfs(node)
            
dfs(0)

print(answer)