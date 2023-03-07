from collections import deque
n,price=map(int,input().split())
coin=deque()
answer=0


for i in range(n):
    start=input()
    coin.appendleft(start)

for i in coin:
    if price==0:
        break
    answer=answer+(price//int(i))
    price=price%int(i)

print(answer)
