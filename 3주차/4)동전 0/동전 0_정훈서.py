n, k = map(int, input().split())
cost = []
answer = 0
for _ in range(n):
    cost.append(int(input()))

# for i in range(n):
#     while k >= cost[n-1-i]:
#         k -= cost[n-1-i]
#         answer += 1
# 시간 초과,,,

for i in range(n):
    if k // cost[n-1-i] > 0: # 몫이 0보다 크다면 = 나눌 수 있다면
        answer += k // cost[n-1-i]
        k = k % cost[n-1-i]

print(answer)