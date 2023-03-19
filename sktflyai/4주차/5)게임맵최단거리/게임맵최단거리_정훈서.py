from collections import deque
def solution(maps):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    n, m = len(maps), len(maps[0])
    x, y = 0, 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and (maps[nx][ny] == 1): # 이동한 좌표가 범위 내에 있고, 벽이 아닌 길이라면
                maps[nx][ny] = maps[x][y] + 1 # 이동한 길이
                queue.append((nx, ny)) # 다음 좌표
    if maps[n-1][m-1] != 1: # 만약 상대 진영까지 이동했다면 1이 아님
        return maps[n-1][m-1]
    else:
        return -1