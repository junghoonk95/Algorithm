n, m = map(int, input().split())
chess_map = []
result = []
for _ in range(n):
    chess_map.append(input())

for i in range(n-7): # 8개만 확인해보기 위해 전체 길이-7
    for j in range(m-7):
        count_same = 0 # 기준점이 지금과 같은 색일 때
        count_diff = 0 # 기준점이 지금과 다른 색일 때
        color = chess_map[i][j] # 기준점 색깔
        for x in range(i, i+8): # 기준점부터 8개 확인
            for y in range(j, j+8):
                if ((i-x)+(j-y)) % 2 == 0: # 기준점과 같은 색이어야 하는 곳이
                    if chess_map[x][y] != color: # 다른 색이라면
                        count_same += 1 # 칠해야 함
                    else: # 기준점이 현재 색이 아닌 다른 색으로 가정, 현재 색과 같은 색이라면
                        count_diff += 1
                else: # 기준점과 다른 색이어야 하는 곳이
                    if chess_map[x][y] == color: # 같은 색이라면
                        count_same += 1 # 칠해야 함
                    else: # 기준점이 현재 색이 아닌 다른 색으로 가정, 현재 색과 다른 색이라면
                        count_diff += 1
        result.append(min(count_same, count_diff)) # result에 더 작은 값 append

print(min(result))