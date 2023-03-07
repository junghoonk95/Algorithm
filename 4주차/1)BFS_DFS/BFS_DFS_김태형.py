from pprint import pprint
from collections import deque
N,M,V = map(int,input().split())
graph = [[] for _ in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
    
graph = list(map(sorted,graph))

visited = [0 for _ in range(N)]
answer = []
is_dfs = False

def dfs(now):
    global is_dfs,answer5
    if is_dfs:
        return
    if len(answer) == N:
        is_dfs = True
        return
    for node in graph[now]:
        if not visited[node] and graph[node]:
            visited[node] = 1
            answer.append(node+1)
            dfs(node)


visited[V-1] = 1
answer.append(V)
dfs(V-1)

for a in answer:
    print(a,end=' ')

visited = [0 for _ in range(N)]
answer = []
visited[V-1] = 1
answer.append(V)
def bfs(now):
    q = deque()
    q.append(now)
    while q:
        if len(answer) == N:
            return
        now = q.popleft()
        for node in graph[now]:
            if not visited[node] and graph[node]:
                visited[node] = 1
                answer.append(node+1)
                q.append(node)

bfs(V-1)
print("")
for a in answer:
    print(a,end=' ')
    
    
''' 깔끔한 풀이
N,M,V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1
    
def dfs(V):
    visited[V] = True
    print(V, end = " ")
    for i in range(1, N+1):
        if not visited[i] and graph[V][i] == 1:
            dfs(i)

def bfs(V):
    visited[V] = False
    queue = [V]
    while queue:
        V = queue.pop(0)
        print(V, end = " ")
        for i in range(1,N+1):
            if visited[i] and graph[V][i] == 1:
                queue.append(i)
                visited[i] = False
    
dfs(V)
print()
bfs(V)
'''