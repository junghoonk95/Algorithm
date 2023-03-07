date = int(input())
# for _ in range(date):
#     answer = 0
#     price = []
#     buy = []
#     n = int(input())
#     price = list(map(int, input().split()))

#     max_index = price.index(max(price))
#     for i in range(max_index):
#         answer += (price[max_index] - price[i])
#     price = price[max_index+1:]
    
#     for i in range(len(price)-1):
#         if price[i] >= price[i+1]: # 내일 값이 오르지 않는다면
#             buy.append(price[i]) # 삼
#         else: # 내일 값이 오른다면
#             if len(price) == 2:
#                 answer += (price[i+1] - price[i])
#             else:
#                 for j in buy:
#                     if j < price[i+1]: # 산 값보다 올랐다면
#                         answer += (price[i+1] - j)

#     print(answer)
# 시간 초과,,,

# 차기 최대값이 이미 지나갔는데, pop으로 차기 최선값으로 이동하면 안 됨
# for _ in range(date):
#     answer = 0
#     _ = int(input())
#     price = list(map(int, input().split()))
#     sorted_price = sorted(price)
#     for j in price:
#         if j < sorted_price[-1]:
#             answer += (sorted_price[-1] - j)
#             sorted_price.remove(j)
#         elif j == sorted_price[-1]:
#             sorted_price.pop()

#     print(answer)
# 또 시간 초과,,,

# for _ in range(date):
#     answer = 0
#     n = int(input())
#     price = list(map(int, input().split()))
#     while len(price) > 1:
#         max_index = price.index(max(price))
#         for i in range(max_index):
#             answer += (price[max_index] - price[i])
#         price = price[max_index+1:]

#     print(answer)
# 또또 시간 초과,,,

# 뒤에서부터 해보자! = 뒤에서부터 확인해가면서 자기보다 값이 같거나 높은게 나올 때까지 다 팔자
for _ in range(date):
    answer = 0
    n = int(input())
    price = list(map(int, input().split()))
    now = price[-1] # 초기값
    for i in range(n-2, -1, -1): # for price in price[::-1]:
        if now > price[i]:
            answer += (now - price[i])
        else:
            now = price[i]
    print(answer)