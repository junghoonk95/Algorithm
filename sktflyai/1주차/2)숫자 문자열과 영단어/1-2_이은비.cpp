#include <string>
#include <vector>

using namespace std;
// zero / one / two, three / four, five / six, seven / eight / nine
bool isAlone(char c) {
    if (c == 'z' || c == 'o' || c == 'e' || c == 'n') return true;
    return false;
}


int solution(string s) {
    int answer = 0;
    
    int idx = 0;
    while (idx < s.length()) {
        // 숫자일때
        if (s[idx]-'0' >= 0 && '9'-s[idx] >= 0) { 
            answer = answer*10 + (s[idx]-'0');
            ++idx;
            continue;
        }
        
        
        // 숫자가 아닐때
        pair<char, int> chg;
        if (isAlone(s[idx])) {
            
            if (s[idx] == 'z') chg = {'0', 4};
            else if (s[idx] == 'o') chg = {'1', 3};
            else if (s[idx] == 'e') chg = {'8', 5};
            else if (s[idx] == 'n') chg = {'9', 4};
            
            answer = answer*10 + (chg.first-'0');
            idx += chg.second;
        }
        else { // two, three / four, five / six, seven
            if (s[idx] == 't') {
                if (s[idx+1] == 'w') chg = {'2', 3};
                else chg = {'3', 5};
            }
            else if (s[idx] == 'f') {
                if (s[idx+1] == 'o') chg = {'4', 4};
                else chg = {'5', 4};
            }
            else if (s[idx] == 's') {
                if (s[idx+1] == 'i') chg = {'6', 3};
                else chg = {'7', 5};
            }
            
            answer = answer*10 + (chg.first-'0');
            idx += chg.second;
        }
        
        
        
    }
    
    
    return answer;
}