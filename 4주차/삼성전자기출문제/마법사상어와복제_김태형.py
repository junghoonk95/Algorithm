M, S = map(int, input().split())

grid = [[0] * 4 for i in range(4)]    #냄새 잡기
dir = {
    1: [0, -1],
    2: [-1, -1],
    3: [-1, 0],
    4: [-1, 1],
    5: [0, 1],
    6: [1, 1],
    7: [1, 0],
    8: [1, -1]
}
shark_dir = {1: [-1, 0], 2: [0, -1], 3: [1, 0], 4: [0, 1]}
fish_dict = {}

for i in range(M):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    if (r, c) in fish_dict:
        fish_dict[(r, c)].append(d)
    else:
        fish_dict[(r, c)] = [d]

s_r, s_c = map(int, input().split())
s_r -= 1
s_c -= 1


def put_fish(loc, new_d, prev_d, fishes):    #물고기 넣기
    r, c = loc
    if (r, c) in fishes:
        fishes[(r, c)].append(new_d)
    else:
        fishes[(r, c)] = [new_d]

    if len(fishes[(r, c)]) == 1:
        fishes.pop((r, c))
    else:
        tmp_fishes = fishes[(r, c)]
        for i in range(len(tmp_fishes)):
            if tmp_fishes[i] == prev_d:
                fishes[(r, c)] = tmp_fishes[:i] + tmp_fishes[i + 1:]
                break
    return fishes


def move(fishes, shark_loc):    #물고기 옮기기
    s_r, s_c = shark_loc
    new_fishes = {}
    for fish in fishes:
        y, x = fish
        prev_ds = fishes[fish]
        for prev_d in prev_ds:
            new_d = prev_d
            cnt = 0
            while True:

                dy, dx = dir[new_d]
                ny, nx = y + dy, x + dx
                if ny >= 0 and ny <= 3 and nx >= 0 and nx <= 3 and grid[ny][nx] == 0 and [ny, nx] != [s_r, s_c]:
                    r, c = ny, nx
                    if (r, c) not in new_fishes:
                        new_fishes[(r, c)] = [new_d]
                    else:
                        new_fishes[(r, c)].append(new_d)

                    break
                else:
                    new_d = (new_d + 7) % 8
                    if new_d == 0:
                        new_d = 8
                cnt += 1
                if cnt == 8:
                    r, c = y, x
                    new_d = prev_d
                    if (r, c) not in new_fishes:
                        new_fishes[(r, c)] = [new_d]
                    else:
                        new_fishes[(r, c)].append(new_d)
                    break
    return new_fishes

def shark_move(fishes, shark_loc, grid):

    import pdb
    # pdb.set_trace()
    grid_shark = [[0] * 4 for i in range(4)]
    for fish in fishes:
        r, c = fish
        grid_shark[r][c] = len(fishes[fish])
    sy, sx = shark_loc

    max_val = 0
    max_grid = {1: [], 2: [], 3: []}
    new_shark_loc = [0, 0]
    first = 0

    for d_key1 in shark_dir:
        dy1, dx1 = shark_dir[d_key1]
        ny1, nx1 = sy + dy1, sx + dx1
        if ny1 < 0 or ny1 > 3 or nx1 < 0 or nx1 > 3:
            continue

        for d_key2 in shark_dir:
            dy2, dx2 = shark_dir[d_key2]
            ny2, nx2 = ny1 + dy2, nx1 + dx2
            if ny2 < 0 or ny2 > 3 or nx2 < 0 or nx2 > 3:
                continue

            for d_key3 in shark_dir:
                dy3, dx3 = shark_dir[d_key3]
                ny3, nx3 = ny2 + dy3, nx2 + dx3
                if ny3 < 0 or ny3 > 3 or nx3 < 0 or nx3 > 3:
                    continue
                first += 1
                set_nynx = set([(ny1, nx1), (ny2, nx2), (ny3, nx3)])
                tmp_val = 0
                for ty, tx in set_nynx:
                    tmp_val += grid_shark[ty][tx]
                if first == 1:
                    max_val = tmp_val
                    max_grid[1] = [ny1, nx1]
                    max_grid[2] = [ny2, nx2]
                    max_grid[3] = [ny3, nx3]
                    new_shark_loc = [ny3, nx3]
                elif max_val < tmp_val:
                    max_val = tmp_val
                    max_grid[1] = [ny1, nx1]
                    max_grid[2] = [ny2, nx2]
                    max_grid[3] = [ny3, nx3]
                    new_shark_loc = [ny3, nx3]
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                grid[i][j] = grid[i][j] - 1

    # print(max_grid)
    for i in max_grid:
        r, c = max_grid[i]
        if grid_shark[r][c] != 0:
            grid[r][c] = 2
        if (r, c) in fishes:
            fishes.pop((r, c))

    return fishes, new_shark_loc, grid


def dup_magic(original_fish_dict, fish_dict):
    for o_r, o_c in original_fish_dict:
        d = original_fish_dict[(o_r, o_c)]
        if (o_r, o_c) in fish_dict:
            fish_dict[(o_r, o_c)].extend(d)
        else:
            fish_dict[(o_r, o_c)] = d
    return fish_dict


for _ in range(S):
    original_fish_dict = fish_dict
    fish_dict = move(fish_dict, [s_r, s_c])    #물고기 이동
    fish_dict, shark_loc, grid = shark_move(fish_dict, [s_r, s_c], grid)    #상어 3칸 이동 및 물고기냄새남김
    fish_dict = dup_magic(original_fish_dict, fish_dict)    #복제마법 완료 및 물고기 냄새 사라짐
    s_r, s_c = shark_loc

print(sum([len(x) for key, x in fish_dict.items()]))