/*
Concept: BFS
먹이까지의 최단거리 계산 이후 가장 상단 왼쪽의 먹이를 골라 먹음
*/

#include<iostream>
#include<queue>
#define INF 1e+09

using namespace std;

queue<pair<int,int>> q;
int vst[21][21], tb[21][21], N;
int sz = 2, sz_cnt = 0;
int answer = 0;

int dx[] = {0, -1, 1, 0};
int dy[] = {-1, 0, 0, 1};

bool isTarget(int x, int y) {
    if(0 < tb[y][x] && tb[y][x] < sz) return true;
    else return false;
}

bool isValid(int x, int y) {
    if (x < 0 || y < 0 || N <= x || N <= y) return false;
    if (vst[y][x] == 1) return false;
    if (tb[y][x] > sz) return false;
    return true;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    
    int x, y;
    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < N; ++j) {
            cin >> tb[i][j];
            if (tb[i][j] == 9) {
                x = j;
                y = i;
            }
        }
    }
    
    //시작점
    q.emplace(x, y);
    vst[y][x] = 1;
    tb[y][x] = 0;
    
    // BFS
    int level = 0;
    while(q.size()) {
        int it = q.size();
        level += 1;
        int targetX = INF, targetY = INF;
        for(int i = 0; i < it; ++i) {
            x = q.front().first;
            y = q.front().second;
            q.pop();

            if(isTarget(x, y)) {
                if(y <= targetY) {
                    //상단
                    if(y != targetY) {
                        targetX = x;
                        targetY = y;
                    }
                    //왼쪽
                    else if(x < targetX) {
                        targetX = x;
                        targetY = y;
                    }
                }
            }

            for(int j = 0; j < 4; ++j) {
                int nextX = x + dx[j];
                int nextY = y + dy[j];

                if(isValid(nextX, nextY)) {
                    q.emplace(nextX, nextY);
                    vst[nextY][nextX] = 1;
                }
            }
        }
        
        if (targetX < 0 || targetY < 0 || N <= targetX || N <= targetY) continue;

        // size와 answer 처리
        if (sz == ++sz_cnt) {
            sz++;
            sz_cnt = 0;
        }
        answer += level - 1;
        
        // queue와 visit, level 초기화
        q = queue<pair<int, int>>();
        fill(&vst[0][0], &vst[20][20], 0);
        level = 0;

        // 새로운 시작점 할당
        q.emplace(targetX, targetY);
        vst[targetY][targetX] = 1;
        tb[targetY][targetX] = 0;
    }

    cout << answer << "\n";
    return 0;
}
