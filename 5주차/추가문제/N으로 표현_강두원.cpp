#include <string>
#include <vector>
#include<iostream>

using namespace std;

const int max_size = 100000;

int dp[max_size];
int N;
int target;
int res = 9;

void dfs(int num, int level) {
    if(num > max_size/2) return;
    if(num < -1 * max_size/2) return;
    if(level > 8) return;

    if(dp[num + max_size/2] <= level) return;
    dp[num + max_size/2] = level;
    
    if(num == target) return;
    
    int nextN = N;

    for(int i = 1; i <= 8 - level; ++i) {
        dfs(num * nextN, level + i);
        dfs(num - nextN, level + i);
        dfs(num / nextN, level + i);
        dfs(num + nextN, level + i);
        nextN = nextN * 10 + N;
    }
}

int solution(int n, int number) {
    N = n, target = number;
    fill(dp, dp+max_size, 9);

    dfs(0, 0);

    return dp[number + max_size/2] > 8 ? -1 : dp[number + max_size/2];
}
