from collections import deque
#배열의 크기 입력받기
n=int(input())
array=[]
#배열 입력받기
for i in range(n):
    array.append(list(map(int,input().split())))

#상어의 크기, x좌표, y좌표
now_size=2
now_x=0
now_y=0

#상어 위치 찾아서 0으로 초기화
for i in range(n):
    for j in range(n):
        if array[i][j]==9:
            now_x=i
            now_y=j
            array[i][j]=0

#bfs로 갈 수 있는 곳 찾기

#이동할 네가지 방향
#(-1,0),(1,0),(0,-1),(0,1) 왼쪽 오른쪽 아래 위
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    dq=deque()
    dq.append((x,y))
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                #가려고 하는 좌표가 now_size보다 작거나 같은 경우만 이동가능
                if array[nx][ny]<=now_size:
                    array[nx][ny]=array[x][y]+1
                    dq.append((nx,ny))
    return array[n-1][n-1]

def findFish():
    check=False
    for i in range(n):
        for j in range(n):
            if array[i][j]>0 and array[i][j]<now_size:
                print(array[i][j])
                check=True
    return check                

print(findFish())
# 만약 전체에 now_size보다 작은 숫자(단, 0보단 큰)가 없으면 종료
# 만약 이동하면서 now_size보다 작은 숫자가 있다면 now_size 와 exp를 비교해서
# 같으면 now_size를 1늘리고 exp를 0으로 초기화한다.
# 동시에 이동한 자리의 숫자를 0으로 초기화한다.
# 이동할때, 숫자가 now_size와 가장 유사한(단 now_size보다 작다)숫자가 가장 우선순위가 높다
