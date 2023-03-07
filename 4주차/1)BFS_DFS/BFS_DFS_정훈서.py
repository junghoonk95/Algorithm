from collections import deque

# n = 정점 개수, m = 간선 개수, v = 탐색 시작점
N, M, V = list(map(int, input().split()))

# 인접 0 행렬 생성 및 초기화
matrix = [[0]*(N+1) for i in range(N+1)]

# 방문한 곳 체크할 리스트
visited_dfs = [0]*(N+1)
visited_bfs = [0]*(N+1)

# 입력받는 값에 대해 0행렬에 1 삽입(인접 리스트 생성)
for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1 # 양방향이기 때문에 [a][b] = [b][a] 둘 다 처리, 입력 받은대로 처리하기에 각각 index가 0인 행과 열은 모두 0

def dfs(V):
    visited_dfs[V] = 1
    print(V, end=' ')
    # 재귀
    for i in range(1, N+1):
        if(visited_dfs[i]==0) and (matrix[V][i]==1): # 아직 방문하지 않았고, 연결되어 있다면
            dfs(i)

def bfs(V):
    # 방문해야 할 곳을 순서대로 넣을 queue
    queue = deque([V])
    visited_bfs[V] = 1
    # 큐 안에 데이터가 없을 때까지
    while queue:
        V = queue.popleft()
        print(V, end=' ')
        for i in range(1, N+1):
            if(visited_bfs[i]==0) and (matrix[V][i]):
                queue.append(i)
                visited_bfs[i] = 1
dfs(V)
print()
bfs(V)