#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int prev = 0, progresses_size = progresses.size(), complete = 0;
    
    while(progresses_size > prev) {
        complete = 0;
        
        for (int i = prev; i < progresses_size; ++i) {
            progresses[i] += speeds[i];
            if (prev >= i && progresses[i] >= 100) {
                ++complete;
                ++prev;
            }
        }
        
        if (complete) answer.push_back(complete);
    }
    
    
    return answer;
}