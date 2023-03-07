def solution(people, limit):
    cnt = 1
    people.sort()
    left = 0
    right = len(people) - 1

    while True:
        if left == right:
            break
        elif left > right:
            cnt -= 1
            break
        
        if people[right] == limit:
            right -= 1
            cnt += 1
        elif people[left] + people[right] > limit: 
            right -= 1
            cnt += 1
        elif people[left] + people[right] <= limit: 
            right -= 1
            left += 1
            cnt += 1

    return cnt

# 최대 두 명 밖에 못 타는데, 최소한으로 필요한 보트 개수 구하는 문제
# 오름차순 정렬 후 인덱스 0번과 -1번을 비교하는 방법으로 경우의 수 나누기
# or 자료구조 deque 사용하기

# 테스트 케이스
people = [50, 70, 80] # 3
limit = 100
print(solution(people, limit))

people = [40, 40, 70, 150] # 3
limit = 150
print(solution(people, limit))

people = [50, 50, 70, 80] #3
limit = 100
print(solution(people, limit))

people = [20, 30, 70, 80, 80] # 3
limit = 100
print(solution(people, limit))