#include <string>
#include <vector>
#include <stack>
#include <iostream>

using namespace std;

int splits(string s, int p) {
    stack<string> st;
    string res = "";
    
    int dup = 0;
    
    for (int i = 0; i < s.length(); i += p) {
        string comp = "";
        
        for (int j = 0; j < p && i+j < s.length(); ++j) {
            comp += s[i+j];
        }
        
        if (!st.empty() && st.top() == comp) {
            ++dup;
        }
        else if (!st.empty()) {
            // top 을 꺼내서 기록.
            res += st.top();
            if (dup > 0) res += (to_string(dup+1));
            st.pop();
            
            // 새로운 top 을 쓴다.
            st.push(comp);
            dup = 0;
        }
        else {
            st.push(comp);
            dup = 0;
        }
    }
    
    if (!st.empty()) {
        // top 을 꺼내서 기록.
        res += st.top();
        if (dup > 0) res += (to_string(dup+1));
        st.pop();
    }
    
    //cout << res << " : ";
    return res.length();
}


int solution(string s) {
    int answer = s.length();
    
    for (int pivot = 1; pivot < s.length(); ++pivot) {
        int n = splits(s, pivot);
        //cout << n << '\n';
        if (answer > n) answer = n;
    }
    
    
    return answer;
}