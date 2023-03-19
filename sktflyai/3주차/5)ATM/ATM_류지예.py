n = int(input())
line = list(map(int, input().split()))
li = sorted(line)

t = 0
sum = 0
for i in li:
    sum += i
    t += sum
print(t)
