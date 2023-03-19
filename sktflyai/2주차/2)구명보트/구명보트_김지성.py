def solution(people, limit):
    # 한 구명보트에 최대 2명
    # 남은 사람 중 가장 무거운 사람 + 가장 가벼운 사람 -> limit보다 무거우면 무거운 사람 혼자 /
    # -> limit보다 안 무거우면 그대로 둘이 보내기
    people.sort()
    answer = 0
    n = 0
    m = len(people) -1
    while n<=m:
        if people[n]+ people[m] <= limit:
            n += 1
        m-=1
        answer += 1
        
    return answer
