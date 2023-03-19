N = int(input()) # 전체 사람 수
people = [[]*(N+1) for _ in range(N+1)]
a, b = map(int, input().split())
visited = [False] * (N+1)
ans = -1
n = int(input())
for _ in range(n):
    p, c = map(int, input().split())
    people[p].append(c)
    people[c].append(p) # 연결된 노드

def dfs(v, num):
    global ans
    num += 1 # 한 촌 수씩 증가
    visited[v] = True # 노드 방문 체크

    if v == b:
        ans += num # 만약 두 번째 사람을 찾았다면 걸린 비용

    for i in people[v]:
        if not visited[i]:
            dfs(i, num)
dfs(a, 0)
print(ans)

# def find_parent(k, list):
#     flag = False
#     for i in range(N):
#         for j in range(len(people[i])):
#             if people[i][j] == k: # 만약 자식 중에 k가 있다면
#                 list.append(i) # 부모 list에 추가
#                 flag = True
#                 break
#         if flag:
#             return list, flag # 만약 상위 부모가 더 있었다면
#     return list, flag # 만약 더 이상 없었다면

# def my_parent(k, list):
#     idx = k
#     flag = True
#     while flag: # 더 이상 현 사람의 부모가 없을 떄까지
#         list, flag = find_parent(idx, list) # 현 사람의 부모 찾기
#         idx = list[-1] # 현 사람을 그 부모로 갱신
#     return list

# a_p = my_parent(a, a_p)
# b_p = my_parent(b, b_p)

# if len(a_p) == 0 and len(b_p) == 0: # 둘 다 최상위면 가족 x
#     print(-1)

# answer = 0 # 초기값(서로 가족이 아닌 경우 체크를 위함)
# for p in a_p:
#     if p in b_p:
#         answer = p
#         break

# if answer == 0:
#     print(-1) # 서로 가족이 아닌 경우
# else: # 가족인 경우
#     a_i = a_p.index(answer)
#     b_i = b_p.index(answer)
#     print(a_i+b_i+2)

# print(people, a_p, b_p)