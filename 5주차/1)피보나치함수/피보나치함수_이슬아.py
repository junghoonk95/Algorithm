num=int(input())

zero=[1,0,1]
one=[0,1,1]
answer=[]
inputnum=[]

for i in range(num):
    inputnum.append(int(input()))

def fibo(x):
    length=len(zero)
    if x>=length:
        for i in range(length,x+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print('{} {}'.format(zero[x],one[x]))
    result=[zero[x],one[x]]
    return result

for i in range(num):
    fibo(inputnum[i])
