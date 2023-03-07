# 실패...
#n 물품 수
#k 무게
from collections import deque

n,k=map(int,input().split())
things=[]
weight=0
value=0

for i in range(n):
    a,b=map(int,input().split())
    things.append((a,b))

#1.무게 순으로 정렬
things.sort()

#모든 물건을 확인하면 종료한다.
for i in things:
    #들고 있는 무게가 한계무게보다 작은 경우에만 실행한다.
    if weight+i[0]<=k:
        weight=weight+i[0]
        value=value+i[1]
    else:
        break
print(value)     
