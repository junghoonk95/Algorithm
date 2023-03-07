# n : 회의 개수, data : 각 회의의 시작시간과 끝나는 시간을 담은 리스트
n = int(input())
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

# 끝나는 시간을 우선순위로 정렬
data.sort(key=lambda data: (data[1], data[0]))


result = 0
tmp = 0
for i in range(n):
    # 끝나는 시간과 그 다음 회의의 시작시간 비교
    if tmp <= data[i][0]:
        result += 1
        tmp = data[i][1] 
print(result)
