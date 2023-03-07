from collections import defaultdict

N, M, K = map(int, input().split())
fireballs = defaultdict(list)

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs[(r-1), (c-1)].append((m, s, d))

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def move_balls():
    # 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동
    global fireballs
    new_fireballs = defaultdict(list)
    for pos, info in fireballs.items():
        r, c = pos
        for m, s, d in info:
            new_r, new_c = (r + s*dr[d]) % N, (c + s*dc[d]) % N
            new_fireballs[(new_r, new_c)].append((m, s, d))
    fireballs = new_fireballs.copy()

def balls_process():
    global fireballs
    new_fireballs = defaultdict(list)

    for pos, info in fireballs.items():
        if len(info) == 1:
            new_fireballs[pos].append(info[0])
            continue

        total_m, total_s, total_d = 0, 0, []
        # 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
        for m, s, d in info:
            total_m += m
            total_s += s
            total_d.append(d)

        # 조건 1) 질량은 ⌊(합쳐진 파이어볼 질량의 합) / 5⌋이다.
        new_m = int(total_m / 5)
        # 조건 2) 속력은 ⌊(합쳐진 파이어볼 속력의 합) / (합쳐진 파이어볼의 개수)⌋이다.
        new_s = int(total_s / len(info))

        # 조건 3) 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
        check = []
        for i in total_d:
            if i%2 == 0:
                check.append(0)
            else:
                check.append(1)
        check = set(check)
        if len(check) == 1:
            new_d_list = [0, 2, 4, 6]
        elif len(check) == 2:
            new_d_list = [1, 3, 5, 7]

        # 조건 4) 질량이 0인 파이어볼은 소멸되어 없어진다.
        if new_m == 0:
            continue
        # 각 방향 값 저장
        for new_d in new_d_list:
            new_fireballs[pos].append((new_m, new_s, new_d))

    fireballs = new_fireballs.copy()

for _ in range(K):
    move_balls()
    balls_process()

res = 0
for pos, info in fireballs.items():
    for m, _, _ in info:
        res += m

print(res)
