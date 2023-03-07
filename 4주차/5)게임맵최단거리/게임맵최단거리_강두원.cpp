#include<iostream>
#include<vector>
#include<queue>

using namespace std;

int N, M;
int s, e;
queue<pair<int, int>> q;
int vst[101][101];
int answer = -1;

int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

int solution(vector<vector<int> > maps)
{
    q.emplace(0, 0);
    vst[0][0] = 1;

    int level = 0;
    int N = maps.size();
    int M = maps[0].size();
    while(q.size()) {
        int it = q.size();
        level++;
        for(int i = 0; i < it; ++i) {
            int curX = q.front().first;
            int curY = q.front().second;
            q.pop();

            if(curY == N-1 && curX == M-1) {
                answer = level;
                return answer;
            }

            for(int j = 0; j < 4; ++j) {
                int nxtX = curX + dx[j];
                int nxtY = curY + dy[j];
                
                if (0<=nxtX && nxtX < M && 0 <= nxtY && nxtY < N && vst[nxtY][nxtX] == 0 && maps[nxtY][nxtX] == 1) {
                    q.emplace(nxtX, nxtY);
                    vst[nxtY][nxtX] = 1;
                }
            }
        }
    }
    return answer;
}
