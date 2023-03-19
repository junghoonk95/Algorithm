#include <string>
#include <vector>
#include <cmath>
using namespace std;
int need[8];
int use[8];
bool check[8]={0,};
int num;
int result=0;

void dfs(int cnt, int remain){
    for(int i=0;i<num;i++){
        if(!check[i] && need[i]<=remain){
            check[i]=1;
            dfs(cnt+1,remain-use[i]);
            check[i]=0;
        }
    }
    result = max(result,cnt);
    return;
}

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    num = dungeons.size();
    for(int i=0;i<num;i++){
        need[i] = dungeons[i][0];
        use[i] = dungeons[i][1];
    }
    dfs(0,k);
    return answer = result;
}
