#include<vector>
#include <queue>
using namespace std;

int n, m;
bool visited[100][100];

bool inRange(int x, int y) {
    return x >= 0 && x < n && y >= 0 && y < m;
}


int solution(vector<vector<int> > maps)
{
    int answer = -1;
    int dx[4] = {-1, 0, 1, 0};
    int dy[4] = {0, 1, 0, -1};
    
    n = maps.size();
    m = maps[0].size();
    
    queue<pair<int, pair<int, int> > > que;
    que.push(make_pair(1, make_pair(0, 0)));
    visited[0][0] = true;
    
    int x, y, step, nx, ny;
    while (!que.empty()) {
        step = que.front().first;
        x = que.front().second.first;
        y = que.front().second.second;
        que.pop();
        
        
        for (int i = 0; i < 4; ++i) {
            nx = x + dx[i];
            ny = y + dy[i];
            if (inRange(nx, ny) && !visited[nx][ny] && maps[nx][ny] == 1) {
                if (nx == n-1 && ny == m-1) return step+1;
                que.push(make_pair(step+1, make_pair(nx, ny)));
                visited[nx][ny] = true;
            }
        }
    }
    
    return answer;
}