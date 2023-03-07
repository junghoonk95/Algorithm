#include <iostream>
#include <algorithm>
using namespace std;

const int Max = 101;

//사람 인원, 간선 개수
int N, M;
//인접 정보
int map[Max][Max];
//정점 방문 여부
bool visited[Max] = { false };
// 촌수
int cnt = -1;
// 입력한 두 사람
int a, b;


int DFS(int a, int b, int c) {
	//방문처리
	visited[a] = true;
	//내가 찾는 애면
	if (a == b) {
		cnt = c;
		return c;
	}

	for (int i = 1; i <= N; i++) {
		if (map[a][i] == 1 && visited[i] == false) {
			//c는 촌수, 내려갈 때 마다 +1
			DFS(i, b, c+1);
		}
	}
	return 0;
}

int main() {
	cin >> N >> a >> b >> M;
	for (int i = 1; i <= M; i++) {
		int x, y;
		cin >> x >> y;
		map[x][y] = 1;
		map[y][x] = 1;
	}

	DFS(a, b, 0);
	cout << cnt;

    return 0;
}
