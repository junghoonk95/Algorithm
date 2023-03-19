n, m = map(int, input().split())
li = [list(input()) for _ in range(n)]

ans = []
for i in range(n-7):
    for j in range(m-7):
        wb_cnt, bw_cnt = 0, 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if li[x][y] != 'B':
                        wb_cnt += 1
                    if li[x][y] != 'W':
                        bw_cnt += 1
                else:
                    if li[x][y] != 'W':
                        wb_cnt += 1
                    if li[x][y] != 'B':
                        bw_cnt += 1
        ans.append(min(bw_cnt, wb_cnt))
print(min(ans)) 

# 정답 배열 만들기
# wb_ans = [list('WB' * 4) for _ in range(8)]
# bw_ans = [list('BW' * 4) for _ in range(8)]
