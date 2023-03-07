N = int(input())
numbers = sorted(list(map(int,input().split())))
tmp = 0
time = 0
for i,t in enumerate(numbers):
    tmp += t
    time += tmp
print(time)
