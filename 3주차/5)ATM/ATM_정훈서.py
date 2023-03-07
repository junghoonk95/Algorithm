n = int(input())

people_time = list(map(int, input().split()))
people_time.sort()
answer = 0

for i in range(n):
    temp = people_time[:i+1]
    answer += sum(temp)

print(answer)