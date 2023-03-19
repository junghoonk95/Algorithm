#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

const int Max = 1001;

//정점, 간선, 시작정점
int N, M, V; 
//인접 정보
int map[Max][Max];
//정점 방문 여부
bool visited[Max] = { false };
//bfs 사용
queue<int> q;


//DFS 구현
void DFS(int v) {
	//방문처리 
	visited[v] = true;
	cout << v << " ";

	//현재 v와 연결되어 있는 정점 확인
	for (int i = 1; i <= N; i++) {
		//연결되어 있고(간선이 있음), 방문하지 않았다면
		if (map[v][i] == 1 && visited[i] == false) {
			DFS(i);
		}
	}
}

//BFS구현
void BFS(int v) {
	//방문처리
	visited[v] = true;
	cout << v << " ";
	//순서 저장할 큐
	q.push(v);

	while (!q.empty()) {
		for (int i = 1; i <= N; i++) {
			//간선이 있고 방문 안했으면
			if (map[v][i] == 1 && visited[i] == false) {
				//큐에 다 넣기
				q.push(i);
				visited[i] = true;
				cout << i << " ";
			}
		}
		q.pop();
		v = q.front();
	}
}

int main() {
	//입력받기
	cin >> N >> M >> V;

	//간선 정보 받기
	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;
		//인접 정보 넣기
		map[a][b] = 1;
		map[b][a] = 1;
	}

	DFS(V);
	for (int i = 1; i <= N; i++) {
		visited[i] = false;
	}
	
	cout << endl;

	BFS(V);

	return 0;
}
