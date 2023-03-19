'''
Concept : Greedy?

짝수 : 4 -> 2 -> 1 -> 1 ...
홀수 : 5 -> 3 -> 2 -> 1 ...
(x/2 의 올림)
이고 a와 b가 같아지는 순간이 만나는 level이므로
반복문을 통해 answer계산
'''

from math import ceil
def solution(n,a,b):
    answer = 0
    
    while a != b:
        a, b = map(lambda x: ceil(x/2), (a,b))
        answer+=1
        
    return answer
