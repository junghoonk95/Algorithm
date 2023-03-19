# 발표여서 코드보고 공부했어요.. 난 못 풀어..
from collections import deque
import heapq

# x, y 좌표의 물고기 잡아 먹고 상어 이동
def eat_fish(x, y):
    global eaten, shark_size, shark
    eaten += 1
    if shark_size == eaten:
        shark_size += 1
        eaten = 0
    graph[x][y] = 0
    shark = [x, y]

def bfs(x, y):
    global shark
    visited = [[False] * n for _ in range(n)]
    fishes = [] # 시간, 행, 열 순으로 저장
    visited[x][y] = True
    q = deque([(x, y, 0)])

    while q:
        cx, cy, t = q.popleft()
        if fishes and t > fishes[0][0]: # 물고기 목록 중에 조건에 맞는 물고기 선택
            second, r, c = heapq.heappop(fishes)
            eat_fish(r, c)
            return second
        if 0 < graph[cx][cy] < shark_size: # 먹을 수 있는 물고기 목록에 추가
            heapq.heappush(fishes, (t, cx, cy))
        for i in range(4):
            nx, ny = cx + d[i][0], cy + d[i][1]
            if nx in range(n) and ny in range(n) and graph[nx][ny] <= shark_size and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, t + 1))
    if fishes:
        second, r, c = fishes[0]
        eat_fish(r, c)
        return second
    else: return None

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
shark = list()
shark_size = 2
eaten = 0
# 상어 위치
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            shark = [i, j]; break

answer = 0
while True:
    time = bfs(*shark)
    if time is None:
        print(answer)
        break
    else: answer += time
