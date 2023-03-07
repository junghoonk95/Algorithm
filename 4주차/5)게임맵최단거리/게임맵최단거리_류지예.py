from collections import deque

def solution(maps):
    len_x, len_y = len(maps), len(maps[0])
    queue = deque([(0, 0)])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 

    while queue:  # bfs
        x, y = queue.popleft()
        for i in range(4):
            xx = x + directions[i][0]
            yy = y + directions[i][1]
            if 0 <= xx < len_x and 0 <= yy < len_y and maps[xx][yy] == 1:
                maps[xx][yy] = maps[x][y] + 1
                queue.append((xx, yy))
    return maps[-1][-1] if maps[-1][-1] > 1 else -1
