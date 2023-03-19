'''
Concept : two-pointer, greedy

greedy 방식으로 현재 가장 무거운 사람과 가장 가벼운 사람이 같이 보트에 탈 수 없을 경우 
그 사람은 무조건 혼자 타야함
'''

def solution(people, limit):
    answer = 0
    
    people.sort()
    lPtr, rPtr = 0, len(people)-1
    
    w = 0
    while lPtr <= rPtr:            
        if people[rPtr] + w <= limit:
            w += people[rPtr]
            rPtr -= 1
        elif people[lPtr] + w <= limit:
            w += people[lPtr]
            lPtr += 1
        else:
            answer += 1
            w = 0
    
    if w > 0:
        answer += 1
    
    return answer



def s(p, t):
    p.sort()
    a, l, r = 0, 0, len(p)-1
    while l <= r:
        l, r, a = l + 1 if p[l] + p[r] <= t else l, r-1, a+1
    
    return a
