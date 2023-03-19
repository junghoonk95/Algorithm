from collections import deque
n=int(input())

time=sorted(map(int,input().split()))
dq=deque(time)
result=0
answer=0

for i in range(n):
    result=result+int(dq.popleft())
    answer=answer+result

print(answer)
