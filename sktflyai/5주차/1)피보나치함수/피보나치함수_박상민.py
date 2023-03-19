import sys
input = sys.stdin.readline

def fib_0(n):
    a = [1, 0]
    a += [0] * (n-1)
    for i in range(2, n+1):
        a[i] = a[i-1] + a[i-2]
    return a[n]

def fib_1(n):
    a = [0, 1]
    a += [0] * (n-1)
    for i in range(2, n+1):
        a[i] = a[i-1] + a[i-2]
    return a[n]

n = int(input())
for _ in range(n):
    m = int(input())
    print('{0} {1}'.format(fib_0(m), fib_1(m)))
