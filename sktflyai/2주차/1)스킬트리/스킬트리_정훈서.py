def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees: # 배열 원소 1개
        chars = ""
        for s in st: # 배열 원소의 알파벳 1개
            if s in skill: # 문자열의 알파벳 1개
                chars += s
        if skill[:len(chars)] == chars: # 문자열의 길이만큼 앞에서 추출했을 때 만들어진 문자열과 같다면, BCD / CBD(O) / CB(O) / BD
            answer += 1
    return answer