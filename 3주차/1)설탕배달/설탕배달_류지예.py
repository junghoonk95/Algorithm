N = int(input())
if N % 5 == 0:
    cnt = N // 5
else:
    x = N // 5
    cnt = -1
    for i in range(x, -1, -1):
        if (N - (5 * i)) % 3 == 0:
            cnt = i + (N - (5 * i)) // 3
            break

print(cnt)
