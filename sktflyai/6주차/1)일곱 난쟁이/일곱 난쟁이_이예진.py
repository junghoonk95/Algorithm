from itertools import combinations
import sys
input = sys.stdin.readline

temp = []
for i in range(9):
    a = int(input())
    temp.append(a)

combi = list(combinations(temp, 2))

for i in range(len(combi)):
    if sum(temp) - sum(combi[i]) == 100:
        for i in combi[i]:
            temp.remove(i)
            
for i in sorted(temp):
    print(i, end = '\n')

    
# 결과는 잘 나오지만 오답 (아마 메모리 비용이 커서 오답이 나오는 것 같습니다.) 
'''
combi = list(combinations(temp, 7))

new = []

for i in (combi):
    if sum(i) == 100:
        for a in i:
            new.append(a)
new = sorted(new)

for i in new:
    print(i, end = '\n')
'''
