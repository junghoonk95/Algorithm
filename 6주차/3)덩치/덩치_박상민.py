import sys
input = sys.stdin.readline
num = int(input())
people = []

for i in range(num):
    people.append(list(map(int, input().split())))

grade = [1 for _ in range(num)]

for i in range(num-1):
    for j in range(i+1, num):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            grade[i] += 1
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            grade[j] += 1

print(*grade)
