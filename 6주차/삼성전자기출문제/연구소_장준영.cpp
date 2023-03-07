#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int hori_len, verti_len;
int map[8][8] = {0, };
int area_n = 0;
int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { -1, 0, 1, 0 };

vector<pair<int, int>> virus;
vector<int> answer;

bool compare(int a, int b)
{
    return a > b;
}
void input()
{
    cin >> verti_len >> hori_len;
    for (int i = 0; i < verti_len; i++)
    {
        for (int j = 0; j < hori_len; j++)
        {
            cin >> map[i][j];
            if (map[i][j] == 0)
                area_n++;
            else if (map[i][j] == 2)
                virus.push_back(make_pair(i, j));
        }
    }
}

void solution()
{
    int map_size = verti_len * hori_len;
    for (int i = 0; i < map_size; i++)
    {
        for (int j = 0; j < map_size; j++)
        {
            if (i == j)
                continue;
            for (int k = 0; k < map_size; k++)
            {
                if (k == i || k == j)
                    continue;
                if (map[i / hori_len][i % hori_len] != 0)
                    continue;
                if (map[j / hori_len][j % hori_len] != 0)
                    continue;
                if (map[k / hori_len][k % hori_len] != 0)
                    continue;
                int safe_area = area_n - 3;
                int visited[8][8] = {0,};
                // 3개의 벽 선택
                visited[i / hori_len][i % hori_len] = 1;
                visited[j / hori_len][j % hori_len] = 1;
                visited[k / hori_len][k % hori_len] = 1;

                // BFS로 안전영역 계산
                queue<pair<int, int>> q;
                // 큐에 virus 저장
                for (int u = 0; u < virus.size(); u++)
                {
                    q.push(make_pair(virus[u].first + dy[0], virus[u].second + dx[0]));
                    q.push(make_pair(virus[u].first + dy[1], virus[u].second + dx[1]));
                    q.push(make_pair(virus[u].first + dy[2], virus[u].second + dx[2]));
                    q.push(make_pair(virus[u].first + dy[3], virus[u].second + dx[3]));
                }
                // bfs
                while (!q.empty())
                {
                    pair<int, int> pre_virus;
                    pre_virus = q.front();
                    q.pop();
                    if (pre_virus.first < 0 || pre_virus.first >= verti_len || pre_virus.second < 0 || pre_virus.second >= hori_len)
                    {
                        // cout << "1" << endl;
                        continue;
                    }
                    if (visited[pre_virus.first][pre_virus.second] == 1)
                    {
                        // cout << "2" << endl;
                        continue;
                    }
                    if (map[pre_virus.first][pre_virus.second] != 0)
                    {
                        continue;
                    }
                    // 영역 감소
                    safe_area -= 1;
                    //cout << safe_area << endl;
                    // 방문 처리
                    visited[pre_virus.first][pre_virus.second] = 1;
                    // 상하좌우
                    q.push(make_pair(pre_virus.first + dy[0], pre_virus.second + dx[0]));
                    q.push(make_pair(pre_virus.first + dy[1], pre_virus.second + dx[1]));
                    q.push(make_pair(pre_virus.first + dy[2], pre_virus.second + dx[2]));
                    q.push(make_pair(pre_virus.first + dy[3], pre_virus.second + dx[3]));
                }
                answer.push_back(safe_area);
                // cout << i << " " << j << " " << k << " " << safe_area << endl;
            }
        }
    }
    sort(answer.begin(), answer.end(), compare);
    cout << answer[0];
           
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    input();
    solution();
}
