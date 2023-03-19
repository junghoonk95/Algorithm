from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)] # N x M 격자
walls = [(r, c) for r in range(N) for c in range(M) if graph[r][c]==0] # 벽의 좌표
walls_c = list(combinations(walls, 3)) # 벽의 좌표 중 3개씩 조합
virus = [(r, c) for r in range(N) for c in range(M) if graph[r][c]==2] # 바이러스 좌표
# 0인 좌표들을 전부 저장하고 3개를 combinations로 선택해서 바이러스 퍼지는거 확인
# 각 경우에 바이러스가 퍼졌을 때 안전 영역의 값을 구하고 최댓값일 경우 갱신
dx = [-1, 1, 0, 0] # 상하
dy = [0, 0, -1, 1] # 좌우
count = 0
answer = 0

def set_walls(): # 2차원 리스트부터는 = 으로는 얕은 복사만 되기 때문에 깊은 복사를 해줘야 원본 값이 안 변함
    global count, answer
    for wall in walls_c: # 조합들에서 한개씩 뽑아
        tmp = copy.deepcopy(graph) # deep copy한 임시 그래프에
        
        for r, c in wall: # 뽑은 좌표에
            tmp[r][c] = 1 # 벽 세우기
        
        for r, c in virus: # 바이러스 
            queue = deque()
            queue.append((r, c))
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nr = x + dx[i]
                    nc = y + dy[i]
                    if (0 <= nr < N and 0 <= nc < M) and tmp[nr][nc] == 0: # 상하좌우를 확인하는데, 좌표 내에 만약 0이 있다면
                        tmp[nr][nc] = 2 # 바이러스 퍼짐
                        queue.append((nr, nc))
        
        for i in range(N):
            for j in range(M):
                if tmp[i][j] == 0: # 안전 영역 개수
                    count += 1
        
        if count > answer: # 최대값이라면 갱신
            answer = count
        
        count = 0 # 리셋

set_walls()
print(answer)
