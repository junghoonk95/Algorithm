#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int N, M, V;
vector<int> edge[1001];
bool visited[1001];

void dfs(int node) {
    cout << node << " ";

    int nxt_node;
    for (int i = 0; i < edge[node].size(); ++i) {
        nxt_node = edge[node][i];
        if (!visited[nxt_node]) {
            visited[nxt_node] = true;
            dfs(nxt_node);
        }
    }
}

void bfs(int node) {
    queue<int> que;
    que.push(node);
    visited[node] = true;

    int nxt_node;
    while (!que.empty()) {
        node = que.front();
        cout << node << " ";
        que.pop();

        for (int i = 0; i < edge[node].size(); ++i) {
            nxt_node = edge[node][i];
            if (!visited[nxt_node]) {
                visited[nxt_node] = true;
                que.push(nxt_node);
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    /* INPUT */
    cin >> N >> M >> V;
    
    int a, b;
    for (int i = 0; i < M; ++i) {
        cin >> a >> b;
        edge[a].push_back(b);
        edge[b].push_back(a);
    }

    /* SOLUTION */
    for (int i = 1; i <= N; ++i) {
        sort(edge[i].begin(), edge[i].end());
    }

    visited[V] = true;
    dfs(V);
    cout << '\n'; fill(visited, visited+1001, false);
    bfs(V);

    return 0;
}