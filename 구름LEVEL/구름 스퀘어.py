n = int(input())

# 행사 정보를 입력받아 종료 시간을 기준으로 오름차순으로 정렬
events = []
for i in range(n):
    start, end = map(int, input().split())
    events.append((start, end))
events.sort(key=lambda x: x[1])
print(events)

# 많은 행사를 선택
count = 0
end_time = 0
for event in events:
    if event[0] >= end_time:
        count = count + 1
        end_time = event[1] + 1 
print(count)
