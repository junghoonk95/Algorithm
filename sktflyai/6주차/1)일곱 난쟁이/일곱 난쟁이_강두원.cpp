#include<iostream>
#include<vector>
#include<numeric>
#include<algorithm>
using namespace std;
int tb[9];
int vst[9];
vector<int> answer;
void dfs(int sum, vector<int> p_vec, int depth) {
    if(accumulate(p_vec.begin(), p_vec.end(), 0) == 100 && depth == 7) p_vec.swap(answer);
    
    for(int i = 0; i < 9; ++i) {
        if(vst[i] == 1) continue;
        vector<int> np_vec(p_vec.size());
        copy(p_vec.begin(), p_vec.end(), np_vec.begin());
        np_vec.push_back(tb[i]);
        vst[i] = 1;
        dfs(sum+tb[i], np_vec, depth+1);
        vst[i] = 0;
    }

}
int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    for(int i = 0; i < 9; ++i) cin >> tb[i];
    
    dfs(0, vector<int>(), 0);
    sort(answer.begin(), answer.end());
    
    for(auto a : answer) cout << a << "\n";
}
