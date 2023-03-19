'''
k층 n호에 사는 사람의 수 출력
'''
T = int(input())

K,N = 14,14

people = [[0 for _ in range(K+1)] for _ in range(N+1)]
people[0] = [i+1 for i in range(14)]

for a in range(1,K+1):
    for b in range(N+1):
        people[a][b] = sum(people[a-1][:b+1])

for _ in range(T):
    k = int(input())
    n = int(input())
    print(people[k][n-1])

# import pprint

# pprint.pprint(people)