from itertools import permutations
def solution(k, dungeons):
    result = []
    save = k
    for i in permutations(dungeons, len(dungeons)): # 순열 이용, 모든 경우의 수 확인(n!이지만 던전의 길이가 최대 8로 충분히 작기에 가능)
        k = save
        answer = 0
        for dungeon in i:
            if dungeon[0] > k:
                continue
            else:
                k -= dungeon[1]
                answer += 1
        result.append(answer)
        
    return max(result)

# def solution(k, dungeons):
#     answer = 0
#     dungeons = sorted(dungeons, key=lambda x: (-(x[0]-x[1]), x[1])) # (최소 필요도 - 소모 필요도) 큰 순서, 같다면 소모 필요도가 작은 순서
#     for dungeon in dungeons:
#         if dungeon[0] > k:
#             continue
#         else:
#             k -= dungeon[1]
#             answer += 1
#     return answer