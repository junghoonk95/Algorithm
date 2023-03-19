import sys
import pprint
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

answer = 0
cnt = 0

def spread_virus(grp):
    q = deque()
    for n in range(N):
        for m in range(M):
            if grp[n][m] == 2:
                q.append((n, m))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M:
                if grp[nx][ny] == 0:
                    grp[nx][ny] = 2
                    q.append((nx, ny))
    return grp


def make_wall():
    global answer
    zeros_pos = []

    for r in range(N):
        for c in range(M):
            if graph[r][c] == 0:
                zeros_pos.append((r, c))

    wall_list = list(combinations(zeros_pos, 3))


    for three_wall in wall_list:
        copy_graph = copy.deepcopy(graph)

        for r, c in three_wall:
            copy_graph[r][c] = -1

        copy_graph = spread_virus(copy_graph)

        temp = 0
        for i in range(N):
            temp += copy_graph[i].count(0)

        if temp > answer:
            answer = temp

make_wall()
print(answer)
