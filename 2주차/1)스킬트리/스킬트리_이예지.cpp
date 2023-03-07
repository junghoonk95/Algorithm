#include <string>
#include <vector>

using namespace std;

int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    string tree = "";
    for(int i =0; i<skill_trees.size(); i++){
        tree = skill_trees[i];
        vector <char> temp;
        for(int j =0; j<tree.size(); j++){
            for(int k = 0; k < skill.size(); k++) {
                if(skill[k] == tree[j]) {
                    //각 스킬트리에서 배울 스킬이 나오면 temp에 push
                    temp.push_back(tree[j]);
                }
            }
        }
        int check = 0;
        //skill과 추출한 temp 비교
        for(int j = 0; j < temp.size(); j++) {
            if(temp[j] != skill[j]) {
                //다르면 check 변경
                check = 1;
                break;
            }
        }
        if(check==0)
            answer++;
    }
    return answer;
}
