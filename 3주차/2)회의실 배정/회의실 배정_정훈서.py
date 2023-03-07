n = int(input())
time_table = []

for _ in range(n):
  s, e = list(map(int, input().split()))
  time_table.append([s, e])

time_table = sorted(time_table, key=lambda x: (x[1], x[0]))
# 회의 시작 시간이 빠른 순서대로, 회의 종료 시간이 빠른 순서대로 정렬

count = 1 # 회의 개수
start = time_table[0][0] # 시작
end = time_table[0][1] # 종료
for i in range(1, n):
  if end <= time_table[i][0]: # 종료 시간과 시작 시간이 동시인 경우도 존재
    end = time_table[i][1]
    count += 1

print(count)