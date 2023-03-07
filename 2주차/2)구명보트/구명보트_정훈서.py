def solution(people, limit):
    answer = 0
    people.sort()
    light = 0
    heavy = len(people) - 1
    
    for _ in range(len(people)):
        if light <= heavy:
            if (people[light] + people[heavy]) <= limit: 
                light += 1
            heavy -= 1
            answer += 1
    
    return answer