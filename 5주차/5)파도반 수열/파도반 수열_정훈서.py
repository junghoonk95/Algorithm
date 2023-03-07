t = int(input())
p = [1, 1, 1, 2, 2]
for _ in range(t):
    n = int(input())
    length = n - 5
    if length <= 0:
        print(p[n-1])
    else:    
        for i in range(length):
            p.append(p[-1]+p[-5])
        print(p[n-1])