#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int N, M, a, b, c, ans;
int parent[1001];
vector<pair<int, pair<int, int> > > edge1; // (cost, (node1, node2))

int find_parent(int node) {
    if (parent[node] == node) return node;
    return parent[node] = find_parent(parent[node]);
}

bool union_find(int node1, int node2) { // 조상 다르면 true
    int node1_p = find_parent(node1);
    int node2_p = find_parent(node2);
    
    if (node1_p != node2_p) {
        if (node1_p < node2_p) {
            parent[node2_p] = node1_p;
        }
        else {
            parent[node1_p] = node2_p;
        }
        return true;
    }
    else return false;
}


void solution1() { // kru : 간선부터 선택
    cin >> N >> M;
    for (int i = 1; i <= N; ++i) {
        parent[i] = i;
    }
    for (int i = 0; i < M; ++i) {
        cin >> a >> b >> c;
        edge1.push_back(make_pair(c, make_pair(a, b)));
    }

    // 간선들(vector<pair<int, pair<int, int> > > edge : (cost, (node1, node2)))을 정렬
    sort(edge1.begin(), edge1.end());
    // 작은 간선부터 선택
    
    for (int i = 0, j = 0; i < M && j < N-1; ++i) {
        a = edge1[i].second.first, b = edge1[i].second.second;
        // 해당 간선에 연결된 노드들이 서로 조상이 같은가? 다른가? (find, parent[i]), 그리고 해당 노드들의 조상 바꿔줌 (Union)
        if (union_find(a, b)) {
            // 다르면 간선 선택하고, 비용 추가
            ++j;
            ans += edge1[i].first;
        }
    }

    cout << ans;
}


int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    solution1();

    return 0;
}
