#include <iostream>

using namespace std;

int solution(int n, int a, int b)
{
    int answer = 0;
    /*
    (a, b 의 번호+1)을 나눈 값이 해당 조의 번호가 된다.
     eg) (1 2) (a 4) (b 6) (7 8)
        (1 a) (b 7)
        (a b)
    만약 조의 번호가 같다면 a, b 가 서로 만났다는 뜻이 된다.
    */
    while (a != b) {
        ++answer;
        a = (a+1)/2;
        b = (b+1)/2;
    }

    return answer;
}