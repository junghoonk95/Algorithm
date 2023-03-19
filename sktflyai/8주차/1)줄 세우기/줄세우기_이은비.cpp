#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;


int N, M, a, b;
int indeg_size[32001];
vector<int> outdeg[32001];

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;
    for (int i = 0; i < M; ++i) {
        cin >> a >> b; // a가 B 앞에. = a -> b
        outdeg[a].push_back(b);
        ++indeg_size[b];
    }

    queue<int> que;
    for (int i = 1; i <= N; ++i) {
        if (indeg_size[i] == 0)
            que.push(i);
    }

    int top, nxt_node;
    while (!que.empty()) {
        // queue에서 빼냄.
        top = que.front();
        que.pop();
        cout << top << " ";
        // 해당 노드가 가리키는 노드들의 수 하나씩 감소시키기.
        for (int i = 0; i < outdeg[top].size(); ++i) {
            nxt_node = outdeg[top][i];
            // 만약 감소시킨 노드의 Indegree가 0 이라면 queue에 넣음.
            if ((--indeg_size[nxt_node]) == 0)
                que.push(nxt_node);
        }
    }

    return 0;
}