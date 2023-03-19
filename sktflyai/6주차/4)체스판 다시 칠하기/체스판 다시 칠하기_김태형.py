N,M = map(int, input().split())
arr = []
arr_min = []

for i in range(N):
    arr.append(input())

for i in range(N-7):
    for j in range(M-7):
        num1 = 0
        num2 = 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2 == 0:
                    if arr[a][b] != 'W':
                        num1 += 1
                    else:
                        num2 += 1
                else:
                    if arr[a][b] != 'B':
                        num1 += 1
                    else:
                        num2 += 1
        arr_min.append(num1)
        arr_min.append(num2)
        
print(min(arr_min))