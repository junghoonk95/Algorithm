'''
NxN 공간, 물고기 M마리, 아기 상어 1마리
한 칸에 물고기 최대 1 마리

아기 상어 
1.최초크기 : 2
2.1초에 상하좌우로 한 칸 이동
3.자신 크기보다 큰 물고기 지나갈 수 없음
    = 자신 크기보다 작거나 같은 크기의 물고기 혹은 빈 공간 지나갈 수 있음
4.자신보다 작은 크기의 물고기만 먹을 수 있음
5.즉 같은 크기의 물고기는 먹을 수 없지만 지나갈 수 있음

이동 결정 방법
1.더 이상 먹을 수 있는 물고기 X -> 엄마 상어 도움 요청(종료 조건)
2.먹을 수 있는 물고기 1마리 -> 해당 물고기로 먹으러 감
3.먹을 수 있는 물고기 1마리보다 많음 -> 거리 가장 가까운 물고기 먹으러감
    -> 거리 가까운 물고기 여러마리면 가장 위,왼쪽 물고기 먹음
    
자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가
먹음과 동시에 크기 1 증가
'''
from collections import deque

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)] #9로 표기된 위치가 아기상어 초기 위치

time = 0
baby_r,baby_c,baby_size = 0,0,2
eat_cnt = 0
fish = []
dr = [0,-1,0,1]
dc = [-1,0,1,0]

visited = [[0 for _ in range(N)] for _ in range(N)]
# 아기상어 초기위치, 물고기들 위치 구하기
for r in range(N):
    for c in range(N):
        if graph[r][c] == 9:
            baby_r,baby_c = r,c
            graph[r][c] = 0
        else:
            if graph[r][c]:
                fish.append((r,c,graph[r][c])) # (r,c,물고기크기)
                

def init_visited():
    for r in range(N):
        for c in range(N):
            visited[r][c] = 0
            
def check_range(r,c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False

def edible_fish():
    edible_list = []
    for r,c,size in fish:
        if size < baby_size and graph[r][c]:
            edible_list.append((r,c,size))
    return edible_list

# bfs를 통해 target 위치로의 최단 거리 구하기
def get_dist(t_r,t_c,now_dist): 
    q = deque()
    q.append((baby_r,baby_c,0))
    init_visited()
    visited[baby_r][baby_c] = 1
    while q:
        r,c,dist = q.popleft()
        if dist > now_dist: # 현재 이미 구해진 tmp_dist보다 bfs를 통해 구하는 dist가 큰 경우 종료(cut-edge)
            return
        if r == t_r and c == t_c: # target에 도착했을 경우 종료
            return dist
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if check_range(nr,nc) and not visited[nr][nc] and baby_size >= graph[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr,nc,dist+1))
                


def eat_target(fish_list):
    global eat_cnt,baby_r,baby_c,baby_size,time,fish
    dist = 9999
    target_r,target_c = -1,-1
    is_tmp_dist = False
    # 먹을 수 있는 모든 물고기에 대해 최단 거리 구하기
    for r,c,size in fish_list:
        tmp_dist = get_dist(r,c,dist)
        if tmp_dist: # get_dist 함수를 통해 최단 거리를 얻을 수 없을 수도 있음(ex.아기상어 크기보다 큰 물고기들로 둘러쌓임)
            if tmp_dist < dist:
                dist = tmp_dist
                target_r,target_c = r,c
                is_tmp_dist = True
    if not is_tmp_dist: # for문을 모두 돌며 한번도 tmp_dist를 얻지 못했을 경우
        fish = [] # main의 while문을 종료시키기 위해 fish list를 빈 list로 초기화
        return # eat_target 함수 종료
    eat_cnt += 1
    if eat_cnt == baby_size:
        baby_size += 1
        eat_cnt = 0
    baby_r,baby_c = target_r,target_c
    time += dist
    graph[target_r][target_c] = 0 # 해당 위치의 물고기 잡아먹음
        
# main
while True:
    edible_list = edible_fish()
    if not edible_list: # 더 이상 먹을 수 있는 물고기가 없으면
        break # while 종료
    eat_target(edible_list)
print(time)


'''
debugging

1. 종료 조건 수정
    1-1. get_dist 함수 통해 최단거리 얻지 못하는 경우 고려(line 92)
    1-2. eat_target()에서 get_dist() 함수의 bfs로 들어갈 때
        bfs에서 현재 tmp_dist보다 큰 dist 갖는 경우 종료하도록 조건 추가(line 71)
        -> 실행시간 : 1100ms -> 476ms, 실제 시험의 제한시간 10초

'''