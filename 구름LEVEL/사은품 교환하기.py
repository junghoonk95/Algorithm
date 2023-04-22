# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
T = int(input())
arr=list(map(int,sys.stdin.readline().split()) for _ in range(T))
def calcu(N,M):

	cnt=min((N+M)//12,N//5)	
	return cnt


for x,y in arr:
	print(calcu(x,y))
	
	
