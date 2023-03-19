from collections import Counter

n = int(input())
people = []
num = []
for _ in range(n):
    x, y = map(int, input().split())
    people.append([x, y])

for i in range(n):
    count = 1
    for j in range(n):
        if j == i: continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]: # 몸무게와 키가 둘 다 큰 경우 = 덩치가 더 큰 경우
            count += 1
    num.append(count) # 본인보다 덩치가 큰 사람의 수
    # 본인이 몇 명보다 덩치가 큰지가 아니라 본인보다 덩치가 큰 사람이 몇 명 있는지가 등수 조건

print(*num) # 리스트를 공백을 기준으로 한 줄로 출력하는 법

# rank = Counter(num)
# rank = sorted(rank.items(), key=lambda x: -x[0])

# start = 1
# for i in range(len(rank)):
#     for j in range(n):
#         if rank[i][0] == num[j]:
#             people[j] = start
#     start += rank[i][1]