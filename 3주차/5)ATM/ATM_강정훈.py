N=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)
a=0
k=0
for i in arr:
    k=k+i
    a=a+k

print(a)
