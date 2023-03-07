#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(string number, int k) {
    string answer = "";

    int ans_size = number.size() - k; // answer 자리 수 
    int index = 0; // 시작 index
    int max_index = 0; //최대 값 index 저장
    
    //answer 자리수 만큼 반복
    for(int i =0; i<ans_size; i++){ 
        char n_max = number[index]; // 최대 값 초기화
        max_index = index; // 최대 값 index 저장
        
        for(int j=index; j<=k+i; j++){
            if(n_max < number[j]){// 최대값 발견
                n_max = number[j]; // 최대값 갱신
                max_index = j; // 최대 index 저장
            }
        }
        index = max_index + 1; //최대값 다음 부터 확인하기
        answer += n_max; // 최대 숫자 저장
    }
    return answer;
}
