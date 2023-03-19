from collections import deque

# n = 컴퓨터 개수, m = 쌍 개수
n = int(input())
m = int(input())

# 행렬 생성 및 초기화
graph = [[]*(n+1) for i in range(n+1)] # 0으로 초기화 하는 경우 bfs에서 조건문 확인 시 visited[0]이 1이 되므로 문제가 됨 -> null로 초기화

# 방문한 곳 체크할 리스트
visited = [0]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a]+=[b]
    graph[b]+=[a] # 양방향 연결
    
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    # 큐 안에 데이터가 없을 때까지
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
    print(sum(visited) - 1)

bfs(graph, 1, visited)