"""

# 1
방문 확인 리스트에, 시작 노드의 값을 True로 변환
# 2 
반복문을 1부터 노드의 개수+1 까지 돈다.
 - 조건 1) 해당 노드를 방문하지 않아야 함(visited 값이 False)
 - 조건 2) 노드의 인접행렬 값이 1이여야 함(graph 값이 1)

ex) 
# V = 3, i = 1~5
graph[3][1] = 1
graph[3][2] = 0
graph[3][3] = 0
graph[3][4] = 1
graph[3][5] = 0

visited = [False][False][False][True(idx : 3)][False][False]

# 노드 개수
N = 5

# 간선 개수
M = 5

# 시작 노드 값
V = 3

"""
import sys

N, M, V = map(int, sys.stdin.readline().rstrip().split())

# 각 노드에 연결 되어 있는 노드를 확인하기 위해 인접행렬 생성
graph = [[0]*(N+1) for _ in range(N+1)]

# 방문 확인을 위한 리스트 생성
visited = [False] * (N+1)

for _ in range(M): #간선의 개수 만큼 만드는 거지?
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1  
    
def dfs(V):
    visited[V] = True
    # print(visited, V)
    print(V, end = ' ')
    for i in range(1, N+1):
        if visited[i] == False and graph[V][i] == 1:
            dfs(i)
            
from collections import deque

def bfs(V):
    visited[V] = False
    queue = deque()
    queue.append(V) 
    
    while queue:
        pop_V = queue.popleft()
        print(pop_V, end = ' ')        
        for i in range(1, N+1):
            if visited[i] == True and graph[pop_V][i] == 1:
                queue.append(i)
                visited[i] = False
                
dfs(V)
print()
bfs(V)
