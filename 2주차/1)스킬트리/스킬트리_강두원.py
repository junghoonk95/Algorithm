'''
concept: Greedy
주어진 스킬트리의 스킬들을 하나씩 보며 현재 찍을 수 없을 경우 불가능한 케이스로 판별
'''

def solution(skill, skill_trees):
    answer = 0
    
    # ASCII 코드기반 index로 변환해주는 함수
    toIdx = lambda x: ord(x) - ord('A')
    
    indegree = [0] * 26
    
    # indegree : 선행 스킬이 몇개인지
    for i, idx in enumerate(list(map(toIdx, skill))):
        indegree[idx] = i+1
        
    for tree in skill_trees:
        degree = 1
        # 일단 answer에 1 더해주고
        answer += 1
        for t in tree:
            if t not in skill:
                continue
            
            if indegree[toIdx(t)] == degree:
                degree += 1
            else:
                # 현재 스킬이 찍을 수 없는 상태일 경우. (불가능한 case)
                answer -= 1
                break
            
            # 선행 스킬이 필요한 스킬을 모두 찍었을 경우
            if degree >= len(skill):
                break
    
    return answer
