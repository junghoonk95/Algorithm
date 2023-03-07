#include <iostream>

using namespace std;

int solution(int n, int a, int b)
{
    int answer = 0;
    for(int i=1; i<n-1; i++){
        answer += 1;
        a = (a+1) / 2; //a의 다음 번호
        b = (b+1) / 2; //b의 다음 번호
        if(a==b)
            break;
    }
    return answer;
}
