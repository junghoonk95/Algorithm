N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))

numbers.sort()

for j in numbers:
    print(j)