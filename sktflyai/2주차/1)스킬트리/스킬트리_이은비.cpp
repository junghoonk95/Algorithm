#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// 자신이 가리키는 노드를 담는 배열
int nxt_node[27];
// 자신을 가리키고 있는 노드의 수를 나타내는 배열
int deg[27];

bool topo(string skill_tree) {
    // indegree 복사
    int deg_copy[27];
    copy(deg, deg + 27, deg_copy);
    
    // 들어온 skill_tree 를 하나씩 탐색하여
    for (int i = 0; i < skill_tree.length(); ++i) {
        int prv_char = skill_tree[i]-'A'+1;
        // 만약 해당 문자의 indegree 가 남아있다면 false 리턴
        if (deg_copy[prv_char] > 0) {
            return false;
        }
        // 가능하다면. 계속 진행
        else {
            --deg_copy[nxt_node[prv_char]];
        }
    }
    // true 리턴
    return true;
}


int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    
    // 들어온 skill 순서대로 위상정렬 indegree 만들기
    for (int i = 1; i < skill.length(); ++i) {
        int nxt = skill[i]-'A'+1;
        int prv = skill[i-1]-'A'+1;
        
        nxt_node[prv] = nxt;
        ++deg[nxt];
    }
    
    // 위상 정렬
    for (int i = 0; i < skill_trees.size(); ++i) {
        if (topo(skill_trees[i])) ++answer;
    }
    
    return answer;
}