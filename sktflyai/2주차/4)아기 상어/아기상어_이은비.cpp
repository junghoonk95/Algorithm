#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int N, shark_x, shark_y, shark_size = 2, shark_cnt = 0;
// shark_x, _y : 아기상어의 좌표. shark_size : 아기상어의 사이즈. shark_cnt : 사이즈업한 뒤에 아기상어가 먹은 물고기수
int board[20][20];
int eat_cnt[8]; // eat_cnt[i] = n : i 사이즈일 때, (경로 상관없이) 먹을 수 있는 물고기의 수

int ans = 0;

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

bool inRange(int x, int y) {
    return x >= 0 && x < N && y >= 0 && y < N;
}

void bfs() {
    queue<pair<int, pair<int, int> > > que; // ( cnt, (x, y) )

    int cnt = 0;
    que.push(make_pair(cnt, make_pair(shark_x, shark_y)));

    bool visited[20][20];
    fill(&visited[0][0], &visited[0][0] + 400, false);
    
    priority_queue<pair<int, int> > p_que; // (x, y). 먹을 수 있는 물고기들을 저장한다.
    // 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다. 
    // => 같은 거리의 (x, y) 물고기쌍들을 오름차순 했을 때 가장 첫 번째 물고기
    bool going = true; 
    // 아직 먹을 수 있는 물고기를 찾지 못 했다면 true
    // 먹을 수 있는 물고기가 존재하면 false -> 나아가지 않고 큐에 남아있는 경로만 탐색한다.

    while(!que.empty()) { // BFS
        int top_cnt = que.front().first;
        int top_x = que.front().second.first;
        int top_y = que.front().second.second;
        que.pop();
        
        for (int i = 0; i < 4; ++i) {
            int new_x = top_x + dx[i];
            int new_y = top_y + dy[i];

            int new_size = board[new_x][new_y];

            // 격자 안이고, 방문하지 않았고, 상어가 지나갈 수 있다면
            if (inRange(new_x, new_y) && !visited[new_x][new_y] && new_size <= shark_size) {
                visited[new_x][new_y] = true;

                if ((new_size == shark_size || new_size == 0)) { // 지나만 간다 (못 먹음)
                    if (going) que.push(make_pair(top_cnt+1, make_pair(new_x, new_y)));
                }
                else { // 먹을 수 있다 (new_size < shark_size)
                    if (cnt != 0 && cnt <= top_cnt) // 만약 먹을 수 있는 물고기들보다 더 가야하는 경로라면, 우선순위큐에 저장하지 않는다.
                        continue;

                    p_que.push(make_pair(-new_x, -new_y));
                    going = false; // 더 나아가기 금지
                    cnt = top_cnt+1;
                }
            }
        }
    }

    if (!p_que.empty()) { // 먹을 수 있는 물고기가 존재한다면
        int new_x = -p_que.top().first;
        int new_y = -p_que.top().second;

        int new_size = board[new_x][new_y];

        board[new_x][new_y] = 0;

        if (++shark_cnt >= shark_size) { // 아기상어의 사이즈 증가 확인
            ++shark_size;
            shark_cnt = 0;
        }

        shark_x = new_x; // 새로운 아기상어의 좌표
        shark_y = new_y;

        for (int k = new_size+1; k < 8; ++k) { // 먹을 수 있는 물고기 수 조절
            --eat_cnt[k];
        }

        ans += (cnt); // 이동한 거리 계산

        return ; // 물고기를 먹으면 BFS, 탐색 종료
    }
}


int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    /* INPUT */
    cin >> N;
    fill(eat_cnt, eat_cnt+8, 0);
    

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> board[i][j];

            if (board[i][j] == 9) { // 아기상어라면,, 좌표를 설정
                shark_x = i;
                shark_y = j;
                board[i][j] = 0;
            }
            else if (board[i][j] != 0) { // 물고기라면, 사이즈 k 일 때 먹을 수 있는 물고기 수에 추가
                for (int k = board[i][j]+1; k < 8; ++k) {
                    ++eat_cnt[k];
                }
                
            }
        }
    }

    /* SOLUTION */
    int can_eat_cnt = eat_cnt[7];
    for (int i = 0; i < can_eat_cnt; ++i) { // 존재하는 물고기 수만큼 탐색을 시행. (한 번의 탐색은 물고기 하나를 먹으면 종료)
        bfs();
    }
    
    cout << ans;

    return 0;
}