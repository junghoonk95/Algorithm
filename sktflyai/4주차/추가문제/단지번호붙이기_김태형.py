from collections import deque
from pprint import pprint

N = int(input())
graph = [list(map(int,list(input()))) for _ in range(N)]

dr = [0,1,0,-1]
dc = [1,0,-1,0]

visited = [[0 for _ in range(N)] for _ in range(N)]

def check(r,c):
    if not visited[r][c] and graph[r][c]:
        return True
    return False

answer = []

for r in range(N):
    for c in range(N):
        if check(r,c):
            visited[r][c] = 1
            q = deque()
            q.append((r,c))
            cnt = 1
            while q:
                rr,cc = q.popleft() # 변수명 주의
                for i in range(4):
                    nr = rr + dr[i]
                    nc = cc + dc[i]
                    if 0 <= nr < N and 0 <= nc < N and check(nr,nc):
                        visited[nr][nc] = 1
                        cnt += 1
                        q.append((nr,nc))
            answer.append(cnt)

print(len(answer))

for a in sorted(answer):
    print(a)
                    