#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool cmp(vector<int> a, vector<int> b) {
    return a[2] < b[2];
}

int parent[101];
int find_parent(int a) {
    if (parent[a] == a) return a;
    else return parent[a] = find_parent(parent[a]);
}

bool union_find(int a, int b) {
    int a_parent = find_parent(a);
    int b_parent = find_parent(b);
    
    if (a_parent == b_parent) return false;
    else {
        parent[b_parent] = a_parent;
        return true;
    }
}


int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    
    for (int i = 1; i <= n; ++i) {
        parent[i] = i;
    }
    sort(costs.begin(), costs.end(), cmp);
    
    int a, b, cost;
    for (int i = 0; i < costs.size(); ++i) {
        a = costs[i][0];
        b = costs[i][1];
        cost = costs[i][2];
        
        if (union_find(a, b)) {
            answer += cost;
        }
    }
    
    return answer;
}