from itertools import permutations as pm
def solution(k, dungeons): # k : 현재 피로도, dungeons : ["최소 필요 피로도, 소모 피로도"]
    n = len(dungeons)
    candidates = list(pm(dungeons,n))
    k_save = k
    res = 0
    for candidate in candidates:
        if res == len(dungeons):
            break
        k = k_save
        cnt = 0
        for dungeon in candidate:
            min_tired,required_tired = dungeon[0],dungeon[1]
            if k >= min_tired:
                cnt += 1
                k -= required_tired
            else:
                break
        if cnt > res:
            res = cnt
    return res