from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        cmp = deque(skill)
        i = 0
        while i < len(tree):
            if tree[i] in cmp:
                if tree[i] in cmp[0]:
                    cmp.popleft()
                else:
                    break
            i += 1
            if i == len(tree):
                answer += 1
    return answer

# 항상 skill 문자열에서 0번 문자와만 비교하면 됨
# 리스트의 0번을 빼내야 하므로 자료구조 deque 사용하기

# 테스트 케이스
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
