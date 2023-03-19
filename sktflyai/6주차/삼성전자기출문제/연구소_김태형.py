from collections import deque
from itertools import combinations
import copy
N,M = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

answer = 0

# 벽 세우기
# def dfs(cnt,sr,sc):
#     if cnt == 3:
#         safe_area()
#         return
#     for r in range(N):
#         for c in range(M):
#             if graph[r][c] == 0 and not visited[r][c]:
#                 visited[r][c] = 1
#                 graph[r][c] = -1
#                 dfs(cnt+1,r,c)
#                 graph[r][c] = 0
#                 visited[r][c] = 0

def set_wall():
    zeros = [(r,c) for r in range(N) for c in range(M) if graph[r][c] == 0]
    list_cb = list(combinations(zeros,3))
    for walls in list_cb:
        for r,c in walls:
            graph[r][c] = -1
        safe_area()
        for r,c in walls:
            graph[r][c] = 0

# 안전 구역 구하기
dr = [1,0,-1,0]
dc = [0,1,0,-1]

def safe_area():
    global answer
    viruses = []
    for r in range(N):
        for c in range(M):
            if graph[r][c] == 2:
                viruses.append((r,c))
    
    # 1. Spread Viruses
    copy_graph = copy.deepcopy(graph)
    for r,c in viruses:
        q = deque()
        q.append((r,c))
        # visited = [[0]*M for _ in range(N)]
        # visited[r][c] = 1
        while q:
            now_r,now_c = q.popleft()
            for i in range(4):
                nr = now_r + dr[i]
                nc = now_c + dc[i]
                if 0 <= nr < N and 0 <= nc < M and copy_graph[nr][nc] == 0:
                    copy_graph[nr][nc] = 2
                    q.append((nr,nc))
    area = 0

    # 2. Get Safe Area
    for r in range(N):
        for c in range(M):
            if copy_graph[r][c] == 0:
                area += 1
    
    copy_graph = []
    if area > answer:
        answer = area

set_wall()

print(answer)