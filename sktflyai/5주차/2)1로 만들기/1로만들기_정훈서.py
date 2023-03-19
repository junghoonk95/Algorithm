# n = int(input())
# count = 0
# while n != 1:
#     count += 1
#     if n % 3 == 1:
#         n -= 1
#     elif n % 3 == 0:
#         n /= 3
#     elif n % 2 == 0:
#         n /= 2

# print(count)
####################### 시간 초과

# n = int(input())
# count = 0
# while n != 1:
#     if n % 3 == 0:
#         n /= 3
#         count += 1
#     if n % 3 == 2 and n % 2 == 0:
#         n /= 2
#         count += 1
#     if n % 3 == 1 and n != 1:
#         n -= 1
#         count += 1

# print(count)
####################### 시간 초과

n = int(input())
d = [0] * (n+1) # 계산 횟수
for i in range(2, n+1): # 1부터 연산
    d[i] = d[i - 1] + 1 # 계산 횟수 + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)	# 1을 더하는 것은 d는 결과가 아닌 계산한 횟수를 저장하기 때문
        # print("{}, 3 나눠지고     {}, {} 중 작은 값".format(i, d[i], d[i//3]+1))
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
        # print("{}, 2 나눠지고     {}, {} 중 작은 값".format(i, d[i], d[i//2]+1))

print(d[n])