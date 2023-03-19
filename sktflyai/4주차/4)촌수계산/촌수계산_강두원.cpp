#include<iostream>
#include<vector>
#include<queue>

using namespace std;
typedef vector<int> vi;

int N, M;
int s, e;
queue<int> q;
vi graph[101];
int vst[101];
int answer = -1;

void bfs() {
    q.push(s);
    vst[s] = 1;

    int level = -1;
    while(q.size()) {
        int it = q.size();
        level++;
        for(int i = 0; i < it; ++i) {
            int cur = q.front();
            q.pop();

            if(cur == e) {
                answer = level;
                return;
            }

            for(auto nxt: graph[cur]) {
                if (vst[nxt] == 0) {
                    q.push(nxt);
                    vst[nxt] = 1;
                }
            }
        }
    }

}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N >> s >> e >> M;

    int t1, t2;
    for(int i = 0; i < M; ++i) {
        cin >> t1 >> t2;
        graph[t1].emplace_back(t2);
        graph[t2].emplace_back(t1);
    }

    bfs();
    cout << answer << "\n";
}
