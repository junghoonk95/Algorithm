#include<iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> st;
    
    int days = 0;
    for(int i = 0; i < progresses.size(); ++i) {
        int p = progresses[i] + (speeds[i] * days);
        if(p < 100) {
            if(st.size() != 0) {
                answer.emplace_back(st.size());
                vector<int>().swap(st);
            }
            days += ceil((100 - p)/(float)speeds[i]);
        }
        st.emplace_back(i);
    }
    
    if(st.size()) 
        answer.emplace_back(st.size());
    
    return answer;
}
