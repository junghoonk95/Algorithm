N=int(input())

def fibo(N):

    if fib0[N] != 9999:   #임의의 큰수

        return [fib0[N],fib1[N]]  # 만약 9999가 아니면 각 0,1 return
    else:

        fib0[N]=fibo(N-1)[0]+fibo(N-2)[0]  # 아니면 각 0,1 값 더해주기
        fib1[N]=fibo(N-1)[1]+fibo(N-2)[1]

        return [fib0[N],fib1[N]]


for i in range(N):
    fib0 = [9999 for i in range(41)]
    fib1 = [9999 for i in range(41)]
    fib0[0] = 1
    fib0[1] = 0
    fib1[0] = 0
    fib1[1] = 1
    a=fibo(int(input()))
    print(a[0],a[1])
    
###############시간초과 버전


N=int(input())
def fibo(N):
    global cnt0,cnt1
    if N == 0:
        cnt0 = cnt0 + 1
        return 0
    elif N == 1:
        cnt1 = cnt1 + 1
        return 1
    else:
        return fibo(N-1)+fibo(N-2)


for i in range(N):
    cnt0=0
    cnt1=0
    fibo(int(input()))
    print(cnt0,cnt1)
