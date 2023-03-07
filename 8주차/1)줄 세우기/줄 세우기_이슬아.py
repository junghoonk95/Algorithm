from collections import deque
n,m=map(int,input().split()) //n은 노드의 개수 m은 간선의 개수
indegree=[0]*(n+1)  //진입차수를 0으로 초기화한다.
number=[[]for _ in range(n+1)] //간선을 담을 리스트


for i in range(m):
    a,b=map(int,input().split())
    number[a].append(b) //a는 시작 노드 b는 도착 노드
    indegree[b]+=1 // 도착 노드 진입차수에 1을 더한다

def topology_sort():
    result=[]
    dq=deque()

    for i in range(1,n+1):
        if indegree[i]==0:
            dq.append(i)  //진입 차수가 0인 노드를 큐에 삽입한다.

    while dq:
        now=dq.popleft() //큐에 있는 첫번째 노드를 꺼낸다
        result.append(now) //결과에 현재 노드를 삽입한다.
        for g in number[now]: 
            indegree[g]-=1  //해당 원소와 연결된 노드들의 진입차수에서 1을 뺀다.
            if indegree[g]==0: //이때 집입차수가 0이면
                dq.append(g) //큐에 현재 노드를 넣는다.

    for res in result:
        print(res, end=' ') //결과를 출력한다.

topology_sort()
