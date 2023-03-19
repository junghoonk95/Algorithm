# def solution(people,limit):
#     people.sort()
#     is_break = False
#     for i in range(len(people)):
#         if people[0] + people[i] > limit:
#             is_break = True
#             break
#     if is_break:
#         i -= 1
#     # i : 첫번째 person과 더했을 때 limit을 넘지 않는 person의 max index
#     saved = len(people) - i - 1
#     boat = saved
#     print(i,saved)
#     for j,person1 in enumerate(people[:i+1]):
#         # print(j,person1,i,boat)
#         if i == j:
#             boat += 1
#             break
#         if saved == len(people):
#             break
#         while person1 + people[i] > limit:
#             saved += 1
#             i -= 1
#         saved += 2
#         boat += 1
#         i -= 1
#     return boat
def solution(people, limit):
    answer = 0
    people.sort()
    start, end = 0, len(people) - 1
    
    while start <= end:
        end -= 1 # 가장 무거운 사람은 무조건 보트에 태움
        answer += 1
        if people[start] + people[end+1] <= limit: # 만약 현재 가장 가벼운 사람이 같이 탈 수 있으면 태움
            start += 1
    return answer
        
    