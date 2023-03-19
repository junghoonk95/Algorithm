#include <string>
#include <vector>

using namespace std;

int dp[500][500];

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    int len = triangle.size();
    
    dp[0][0] = triangle[0][0];
    
    for (int i = 0; i < len-1; ++i) {
        for (int j = 0; j <= i; ++j) {
            dp[i+1][j] = max(dp[i][j] + triangle[i+1][j], dp[i+1][j]);
            dp[i+1][j+1] = max(dp[i][j] + triangle[i+1][j+1], dp[i+1][j+1]);
        }
    }
    
    for (int i = 0; i < len; ++i) {
        answer = max(answer, dp[len-1][i]);
    }
    
    return answer;
}