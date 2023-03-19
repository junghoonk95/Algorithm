from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
ans = []

def bfs(queue, cnt): # 1인 노드들만 방문하고 cnt 구하기
    while queue:
        vr, vc = queue.popleft()
        graph[vr][vc] = 0

        for i in range(4): # 인접한 노드 큐에 추가하기
            nx = vr + dx[i]
            ny = vc + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt += 1
                queue.append([nx, ny])
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            ans.append(bfs(deque([[i, j]]), 1))

print(len(ans))
for x in sorted(ans):
    print(x)
