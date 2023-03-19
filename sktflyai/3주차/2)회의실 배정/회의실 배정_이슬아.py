n=int(input())
time=[]
endtime=[]

for i in range(n):
    start,end=map(int,input().split())
    time.append((start,end))

time.sort(key=lambda x:(x[1],x[0]))

#끝나는 시간 기준으로 작은 순으로 정렬한 다음, 시작 시간이 작은 걸 고르기
count=0
result=-1
for i in range(n):
    if time[i][0]>=result:
        result=time[i][1]
        count=count+1

print(count)
