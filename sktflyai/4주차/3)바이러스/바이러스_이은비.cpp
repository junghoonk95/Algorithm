#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
#define virus 1

int N, M, a, b, ans = 0;
vector<int> edge[101];
int visited[101];

int parent[101];

void solution1() { // BFS
    /* INPUT */
    for (int i = 0; i < M; ++i) {
        cin >> a >> b;
        edge[a].push_back(b);
        edge[b].push_back(a);
    }

    /* SOLUTION */
    queue<int> que;
    que.push(virus);
    visited[virus] = true;

    int node, nxt_node;
    while (!que.empty()) {
        node = que.front();
        que.pop();

        for (int i = 0; i < edge[node].size(); ++i) {
            nxt_node = edge[node][i];
            if (!visited[nxt_node]) {
                visited[nxt_node] = true;
                que.push(nxt_node);
                ++ans;
            }
        }
    }
}

// --------------------------------------

int find_parent(int node) {
    if (parent[node] == node) return node;
    else return parent[node] = find_parent(parent[node]);
}

void union_(int node1, int node2) {
    if (node1 < node2) parent[node2] = node1;
    else parent[node1] = node2;
}

void solution2() { // union-find
    for (int i = 1; i <= N; ++i) {
        parent[i] = i;
    }
    
    int a_parent, b_parent;
    for (int i = 0; i < M; ++i) {
        cin >> a >> b;

        a_parent = find_parent(a);
        b_parent = find_parent(b);

        if (a_parent > b_parent)
            union_(a_parent, b_parent);
        else
            union_(b_parent, a_parent);
    }

    for (int i = 2; i <= N; ++i) {
        if (find_parent(i) == virus) ++ans;
    }
}


int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    /* INPUT */
    cin >> N >> M;

    /* SOLUTION */
    solution2();

    cout << ans;

    return 0;
}