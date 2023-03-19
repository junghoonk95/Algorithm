#include <string>
#include <vector>
#include <deque>
#include <iostream>

using namespace std;
deque<int> st;

string solution(string number, int k) {
    string answer = "";
    
    int num;
    
    for (int i = 0; i < number.length(); ++i) {
        num = number[i] - '0';
        
        // stack 에 있는 것이 현재 수보다 작은것이라면 모두 빼냄.
        while (k > 0 && !st.empty() && st.back() < num) {
            st.pop_back();
            --k;
        }
        
        st.push_back(num);
    }
    
    while (k > 0 && !st.empty()) { // 테케 : "4321", 1, "432"
        st.pop_back();
        --k;
    }
    
    while (!st.empty()) {
        answer += (st.front() + '0');
        st.pop_front();
    }
    
    return answer;
}