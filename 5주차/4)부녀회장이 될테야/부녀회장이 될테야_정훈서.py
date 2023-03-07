t = int(input())
for _ in range(t):
    k = int(input()) # 층
    n = int(input()) # 호
    people = [[0 for _ in range(n)] for _ in range(k+1)]
    for i in range(k+1):
        for j in range(n):
            if i == 0:
                people[i][j] = j+1
            else:
                for a in range(j+1):
                    people[i][j] += people[i-1][a]
    print(people[k][n-1])