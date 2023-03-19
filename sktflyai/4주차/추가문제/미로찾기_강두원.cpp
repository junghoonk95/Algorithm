#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>

using namespace std;

int N, M, answer;
queue<pair<int,int>> q;
int tb[100][100], vst[100][100];
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

void bfs(int x, int y) {
    queue<pair<int, int>>().swap(q);
    q.emplace(x, y);
    vst[y][x] = 1;
    int cnt = 0;

    while(q.size()) {
        cnt++;
        int qSize = q.size();
        for(int i = 0; i < qSize; ++i) {
            int curX = q.front().first;
            int curY = q.front().second;
            q.pop();

            if(curX == M-1 && curY == N-1) {
                answer = cnt;
                return;
            }

            for(int j = 0; j < 4; ++j) {
                int nxtX = curX + dx[j];
                int nxtY = curY + dy[j];

                if(0 <= nxtX && nxtX < M && 0 <= nxtY && nxtY < N && tb[nxtY][nxtX] == 1 && vst[nxtY][nxtX] == 0) {
                    vst[nxtY][nxtX] = 1;
                    q.emplace(nxtX, nxtY);
                }
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;

    string temp;
    for(int i = 0; i < N; ++i) {
        cin >> temp;
        for(int j = 0; j < temp.size(); ++j) {
            tb[i][j] = temp[j] - '0';
        }
    }

    bfs(0, 0);
    cout << answer << "\n";
}
