'''
3키로 봉지, 5키로 봉지
'''
import sys
N = int(input())

if N%5 == 0:
    print(N//5)
    sys.exit()
for i in range(1,N//3+1):
    left = N-3*i
    if left%5 == 0:
        print(i+left//5)
        sys.exit()
    elif left == 0:
        print(i)
        sys.exit()
print(-1)