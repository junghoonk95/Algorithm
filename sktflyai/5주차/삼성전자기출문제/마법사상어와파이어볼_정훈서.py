N, M, K = map(int, input().split()) # N:격자, M:파이어볼 개수, K:이동 횟수

graph = [[[] for _ in range(N)] for _ in range(N)] # N x N 격자
fire_ball = [] # x, y, 중량, 속력, 방향
for i in range(M):
    x, y, m, s, d = list(map(int, input().split()))
    fire_ball.append([x-1, y-1, m, s, d])

# (x, y) 좌표 격자에서 위/아래 = x, 왼쪽/오른쪽 = y
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
# 방향 0  1  2  3  4   5  6   7

for _ in range(K): # K번만큼 시행
    while fire_ball: # 각 파이어볼 이동
        r, c, m, s, d = fire_ball.pop(0)
        nr = (r + s * dx[d]) % N  # 1번-N번 행 연결
        nc = (c + s * dy[d]) % N
        graph[nr][nc].append([m, s, d])

    for r in range(N): # 전체 맵을 순회하며
        for c in range(N):
            if len(graph[r][c]) > 1: # 해당 좌표에 파이어볼 2개 이상인 경우
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(graph[r][c])
                while graph[r][c]:
                    m, s, d = graph[r][c].pop() # 하나씩 꺼내기
                    sum_m += m # 무게
                    sum_s += s # 속력
                    if d % 2: # 홀수 방향
                        cnt_odd += 1
                    else: # 짝수 방향
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt: # 방향이 모두 짝수/홀수인 경우
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m // 5: # 나눠진 질량이 0이 아니라면
                    for d in nd: # 4개의 파이어볼로 나눠짐
                        fire_ball.append([r, c, sum_m//5, sum_s//cnt, d])

            elif len(graph[r][c]) == 1: # 해당 좌표에 파이어볼이 1개인 경우
                fire_ball.append([r, c] + graph[r][c].pop()) # 그대로 append

print(sum([ball[2] for ball in fire_ball])) # K번 이동 후 존재하는 파이어볼의 무게 합 출력



# def init_graph():
#     global graph
#     graph = [[[] for _ in range(N)] for _ in range(N)]

# def ball_move():
#     init_graph()
#     for i in range(M):
#         # x 좌표
#         if fire_ball[i][4] == 1 or fire_ball[i][4] == 2 or fire_ball[i][4] == 3:
#             fire_ball[i][1] += fire_ball[i][3]
#             fire_ball[i][1] %= N # N번 행과 1번 행 연결
#         elif fire_ball[i][4] == 5 or fire_ball[i][4] == 6 or fire_ball[i][4] == 7:
#             fire_ball[i][1] -= fire_ball[i][3]
#             if fire_ball[i][1] <= 0:    
#                 fire_ball[i][1] += N # 1번 행과 N번 행 연결
#         # y 좌표
#         if fire_ball[i][4] == 3 or fire_ball[i][4] == 4 or fire_ball[i][4] == 5:
#             fire_ball[i][0] += fire_ball[i][3]
#             fire_ball[i][0] %= N # N번 열과 1번 열 연결
#         elif fire_ball[i][4] == 0 or fire_ball[i][4] == 1 or fire_ball[i][4] == 7:
#             fire_ball[i][0] -= fire_ball[i][3]
#             if fire_ball[i][0] <= 0:    
#                 fire_ball[i][0] += N # 1번 열과 N번 열 연결
#         graph[fire_ball[i][0]][fire_ball[i][1]].append([fire_ball[i][2], fire_ball[i][3], fire_ball[i][4]]) # 무게, 속력, 방향
    
    # for i in range(M): # 겹치는지 확인
    #     tmp = [] # 겹치는 파이어볼
    #     for j in range(M):
    #         if i == j:
    #             continue
    #         if check[fire_ball[i][0]-1][fire_ball[i][1]-1] == 0: # 아직 비교 안 해본 좌표이고
    #             if fire_ball[i][0] == fire_ball[j][0]: # x 좌표가 겹치는데
    #                 if fire_ball[i][1] == fire_ball[j][1]: # y 좌표도 겹치는게 있다면
    #                     graph[fire_ball[j][0]-1][fire_ball[j][1]-1] += fire_ball[j][2]
    #                     tmp.append(j)
    #     if graph[fire_ball[i][0]-1][fire_ball[i][1]-1] != 0:
    #         graph[fire_ball[i][0]-1][fire_ball[i][1]-1] += fire_ball[i][2]
    #         tmp.append(i)
    #         check[fire_ball[i][0]-1][fire_ball[i][1]-1] = tmp # 해당 좌표에 겹치는 파이어볼
    
    # for i in range(M):
    #     for j in range(M):
    #         if graph[i][j] != 0: # 겹치는게 있는 좌표라면
    
    # m, s = 0
    # for i in range(M):
    #     if len(check[fire_ball[i][0]][fire_ball[i][1]]) > 1: # 겹치는게 있다면
    #         for j in range(len(check[fire_ball[i][0]][fire_ball[i][1]])):
    #             m += fire_ball[check[fire_ball[i][0]][fire_ball[i][1]][j]][2]
    #             s += fire_ball[check[fire_ball[i][0]][fire_ball[i][1]][j]][3]
    #         m = int(m/5)
    #         s = int(s/len(check[fire_ball[i][0]][fire_ball[i][1]]))
    #         if m > 0:
    #             for j in range(len(check[fire_ball[i][0]][fire_ball[i][1]])): # 겹치는게 있다면
    #                 fire_ball.pop(check[fire_ball[i][0]][fire_ball[i][1]][j])
    #             fire_ball.append([fire_ball[i][0], fire_ball[i][1], m, ])
    # for x in range(N):
    #     for y in range(N):
    #         if len(graph[x][y]) > 1: # 겹치는게 있다면
    #             m, s, o, e = 0, 0, 0, 0 # 무게, 속력, 방향(짝수), 방향(홀수)
    #             for i in range(len(graph[x][y])):
    #                 m += graph[x][y][i][0]
    #                 s += graph[x][y][i][1]
    #                 if graph[x][y][i][2] % 2: # 홀수
    #                     o += 1
    #                 else: # 짝수
    #                     e += 1
    #             m = int(m/5)
    #             s = int(s/len(graph[x][y]))
    #             if o == len(graph[x][y]) or e == len(graph[x][y]): # 방향이 전부 짝수이거나 홀수인 경우
    #                 d = [0, 2, 4, 6]
    #             else:
    #                 d = [1, 3, 5, 7]
                
    #             for ball in fire_ball[::]: # 해당 좌표에서 합쳐진 파이어볼 제거
    #                 if ball[0] == x and ball[1] == y:
    #                     fire_ball.remove(ball)
    #             if m > 0:
    #                 for i in range(4): # 4개로 쪼개진 파이어볼 추가
    #                     fire_ball.append([x, y, m, s, d[i]])

# for _ in range(K):
#     ball_move()