# N = int(input())

# def count_fibonacci(n):
#     global count_zero, count_one
#     if n == 0:
#         count_zero += 1
#         return 0
#     elif n == 1:
#         count_one += 1
#         return 1
#     else:
#         return (count_fibonacci(n-1) + count_fibonacci(n-2))

# for _ in range(N):
#     k = int(input())
#     count_zero = 0
#     count_one = 0
#     count_fibonacci(k)
#     print(count_zero, count_one)
########################################################## 시간 초과

# 
# 0 - 1 0
# 1 - 0 1
# 2 - 1 1
# 3 - 1 2
# 4 - 2 3
# 5 - 3 5
# 6 - 5 8
# 7 - 8 13
# 8 - 13 21
# 9 - 21 34
# 10 - 34 55

N = int(input())

def count_fibo(n):
    global count_zero, count_one
    tmp = 0
    for _ in range(n):
        tmp = count_zero
        count_zero = count_one
        count_one += tmp

for _ in range(N):
    count_zero, count_one = 1, 0
    count_fibo(int(input()))
    print(count_zero, count_one)