from collections import deque
n, m, v = map(int, input().split())
input_li = [list(map(int, input().split())) for _ in range(m)]

# 연결되어 있는 노드들을 그래프로 표현
graph = [[] for _ in range(n+1)]
for x in input_li:
    graph[x[0]].append(x[1])
    graph[x[1]].append(x[0])
for x in graph:
    x.sort()

visited = [False for _ in range(n+1)]
def dfs(graph, v):
    visited[v] = True # 현재 노드 방문 처리
    print(v, end=" ")
    for x in graph[v]: # 현재 노드와 연결된 노드 방문하기
        if not visited[x]:
            dfs(graph, x)

def bfs(graph, start):
    visited = [False for _ in range(n+1)]
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]: # 인접한 노드들 중 방문하지 않은 노드 큐에 추가
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                
        
dfs(graph, v)
print()
bfs(graph, v)