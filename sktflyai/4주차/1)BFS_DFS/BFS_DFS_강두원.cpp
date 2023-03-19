#include<iostream>
#include<queue>

using namespace std;
#define MAX_SIZE 1001

int tb[MAX_SIZE][MAX_SIZE];
int vst[MAX_SIZE];
int N, M, V;
queue<int> q;

void dfs(int cur) {
    cout << cur << " ";
    for(int i = 1; i <= N; ++i) {
        if(tb[cur][i] == 1 && vst[i] == 0) {
            vst[i] = 1;
            dfs(i);
        }
    }
}

void bfs(int st) {
    q.push(st);
    vst[st] = 1;

    while (q.size()) {
        int cur = q.front();
        q.pop();
        cout << cur << " ";
        for(int i = 1; i <= N; ++i) {
            if(tb[cur][i] == 1 && vst[i] == 0) {
                q.push(i);
                vst[i] = 1;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M >> V;

    int s, e;

    for(int i = 0; i < M; ++i) {
        cin >> s >> e;
        tb[s][e] = 1;
        tb[e][s] = 1;
    }

    vst[V] = 1;
    dfs(V);
    cout << "\n";

    fill(vst, vst+MAX_SIZE, 0);

    bfs(V);
    cout << "\n";
}
