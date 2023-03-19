from collections import deque

def solution(maps):
    q = deque()
    q.append((0,0,0))
    N,M = len(maps),len(maps[0])
    visited = [[0]*M for _ in range(N)]
    dr,dc = [0,1,0,-1],[1,0,-1,0]
    while q:
        r,c,cnt = q.popleft()
        if r == N-1 and c == M-1:
            return cnt+1
        for i in range(4):
            nr,nc = r + dr[i],c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maps[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr,nc,cnt+1))
    return -1
                