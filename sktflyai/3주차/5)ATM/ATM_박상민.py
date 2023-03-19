n = int(input())
p = list(map(int, input().split()))
p.sort(reverse=True)
tot = 0
for i in range(1, len(p)+1):
    tot += p[i-1] * i 
print(tot)
