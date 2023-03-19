#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>

using namespace std;

int N;
queue<pair<int,int>> q;
int tb[25][25], vst[25][25];
vector<int> v;
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

void bfs(int x, int y) {
    queue<pair<int, int>>().swap(q);
    q.emplace(x, y);
    vst[y][x] = 1;
    int cnt = 0;
    while(q.size()) {
        int curX = q.front().first;
        int curY = q.front().second;
        q.pop();
        cnt++;

        for(int i = 0; i < 4; ++i) {
            int nxtX = curX + dx[i];
            int nxtY = curY + dy[i];

            if(0 <= nxtX && nxtX < N && 0 <= nxtY && nxtY < N && tb[nxtY][nxtX] == 1 && vst[nxtY][nxtX] == 0) {
                vst[nxtY][nxtX] = 1;
                q.emplace(nxtX, nxtY);
            }
        }
    }
    v.emplace_back(cnt);
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N;

    string temp;
    for(int i = 0; i < N; ++i) {
        cin >> temp;
        for(int j = 0; j < temp.size(); ++j) {
            tb[i][j] = temp[j] - '0';
        }
    }

    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < N; ++j) {
            if(vst[i][j]==0 && tb[i][j]==1){
                bfs(j, i);
            }   
        }
    }

    sort(v.begin(), v.end());

    cout << v.size() << "\n";
    
    for(auto n : v) {
        cout << n << "\n";
    }
}
