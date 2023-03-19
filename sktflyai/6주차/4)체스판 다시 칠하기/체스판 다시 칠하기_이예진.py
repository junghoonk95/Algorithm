import sys

input = sys.stdin.readline

N, M = map(int, input().split())
chess = [input() for _ in range(N)]
check = []

for row in range(N-7):
    for col in range(M-7):
        first_w = 0
        first_b = 0
        for i in range(row, row+8):
            for j in range(col, col+8):
                if (i+j) % 2 == 0:
                    if chess[i][j] != 'W':
                        first_w += 1
                    if chess[i][j] != 'B':
                        first_b += 1
                else:
                    if chess[i][j] != 'B':
                        first_w += 1
                    if chess[i][j] != 'W':
                        first_b += 1
        check.append(first_w)
        check.append(first_b)
print(check)
print(min(check))

