#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int num;
bool visited[8];
vector<string> list_;


void perm(string str) {
    if (str.size() >= num) {
        list_.push_back(str);
        return ;
    }
    
    for (int i = 0; i < num; ++i) {
        if (!visited[i]) {
            visited[i] = true;
            perm(str+to_string(i));
            visited[i] = false;
        }
    }
}


int solution(int k, vector<vector<int>> dungeons) {
    int answer = 0;
    num = dungeons.size();
    
    perm("");
    for (int i = 0; i < list_.size(); ++i) {
        int power = k;
        int cnt = 0;
        for (int j = 0; j < list_[i].size(); ++j) {
            if (dungeons[list_[i][j]-'0'][0] <= power) {
                power -= dungeons[list_[i][j]-'0'][1];
                ++cnt;
            }
        }
        answer = max(answer, cnt);
    }
    
    return answer;
}