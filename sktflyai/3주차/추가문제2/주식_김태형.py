import random
import pprint
T = int(input())
tc = []
for _ in range(T):
# while True:
    N = int(input())
    prices = list(map(int,input().split()))
    # N = random.randint(2,5)
    # prices = [random.randint(1,10) for i in range(N)]
    # original = list(map(str,prices))
    cnt = 0
    price_max = 0
    for price in prices[::-1]:
        if price < price_max:
            cnt += price_max - price
        if price > price_max:
            price_max = price

    # sort_prices = sorted(prices)
    # # tmp = 0
    # for price in prices:
    #     if price < sort_prices[-1]:
    #         cnt += sort_prices[-1] - price
    #     elif price == sort_prices[-1]:
    #     # else:  #price == sort_prices[-1]:
    #         sort_prices.pop()

    print(int(cnt))

#     # 시간 초과 풀이
#     cnt2 = 0
#     while len(prices)>1:
#         idx = prices.index(max(prices))
#         cnt2 += sum([prices[idx]-price for price in prices[:idx]])
#         # cnt += sum(prices[:idx])
#         prices = prices[idx+1:]
#     # print(cnt)
#     if cnt != cnt2:
#         tc.append(str(N) + "\n")
#         tc.append(" ".join(original))
#         break
#     print(cnt,cnt2)
# dir = './test.txt'
# # tc = list(map(str,tc))
# # file = open('dir','w')
# with open(dir,'w') as file:
#     file.writelines(tc)
