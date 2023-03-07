#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

const int Max = 101;

//컴퓨터 개수, 간선 개수
int N, M;
//인접 정보
int map[Max][Max];
//정점 방문 여부
bool visited[Max] = { false };
//bfs 사용
queue<int> q;
// 바이러스 걸린 컴퓨터 개수
int cnt = 0;


int BFS(int v) {
	//방문처리
	visited[v] = true;
	//순서 저장할 큐
	q.push(v);

	while (!q.empty()) {
		for (int i = 1; i <= N; i++) {
			//간선이 있고 방문 안했으면
			if (map[v][i] == 1 && visited[i] == false) {
				//큐에 다 넣기
				q.push(i);
				cnt++;
				visited[i] = true;
			}
		}
		q.pop();
		v = q.front();
	}
	return cnt;
}

int main() {
	cin >> N >> M;
	for (int i = 1; i <= M; i++) {
		int a, b;
		cin >> a >> b;
		map[a][b] = 1;
		map[b][a] = 1;
	}

	cout << BFS(1);

    return 0;
}
