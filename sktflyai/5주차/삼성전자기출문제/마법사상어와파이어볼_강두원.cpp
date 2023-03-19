#include <iostream>
#include <vector>
using namespace std;

int N, M, K;

typedef struct at {
    int m;
    int s;
    int d;
} at;

typedef vector<at> va;
typedef vector<va> vva;
typedef vector<vva> vvva;

vvva at_vec;

int dx[] = {0, 1, 1, 1, 0, -1, -1, -1};
int dy[] = {-1, -1, 0, 1, 1, 1, 0, -1};

int trans_coord(int x) {
    while(x<0) x+=N;
    return x % N;
}

void move() {
    vvva temp_vec;
    vvva(N, vva(N)).swap(temp_vec);

    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < N; ++j) {
            for(int k = 0; k < at_vec[i][j].size(); ++k) {
                int cm = at_vec[i][j][k].m;
                int cs = at_vec[i][j][k].s;
                int cd = at_vec[i][j][k].d;

                int nx = trans_coord(j + cs * dx[cd]);
                int ny = trans_coord(i + cs * dy[cd]);
                temp_vec[ny][nx].push_back({cm, cs, cd});
            }
        }
    }

    temp_vec.swap(at_vec);
}

int merge_split() {
    vvva temp_vec;
    vvva(N, vva(N)).swap(temp_vec);
    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < N; ++j) {
            int aNum = at_vec[i][j].size();
            int sd = 0, ss = 0, sm = 0;
            if (aNum < 2) {
                if(aNum == 1) temp_vec[i][j].push_back(at_vec[i][j][0]);
                continue;
            }

            for(int k = 0; k < aNum; ++k) {
                sm += at_vec[i][j][k].m;
                ss += at_vec[i][j][k].s;
                if(at_vec[i][j][k].d & 1) sd++;
            }

            int nm = sm/5;
            int ns = ss/aNum;
            if (nm == 0) continue;

            for(int k = 0; k < 4; ++k) {
                temp_vec[i][j].push_back({nm, ns, k*2 + sd%aNum});
            }
        }
    }
    temp_vec.swap(at_vec);
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N >> M >> K;
    int x, y, m, s, d;
    int answer = 0;
    vvva(N, vva(N)).swap(at_vec);
    
    for(int i = 0; i < M; ++i) {
        cin >> y >> x >> m >> s >> d;
        at_vec[y-1][x-1].push_back({m, s, d});
    }

    for(int i = 0; i < K; ++i) {
        move();
        merge_split();
    }

    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < N; ++j) {
            for(int k = 0; k < at_vec[i][j].size(); ++k) {
                answer += at_vec[i][j][k].m;
            }
        }
    }

    cout << answer << "\n";
    return 0;
}

/*
실수 
1. 칸 안에 원자가 1개일 경우 옮겨주지 않았음
2. 좌표 계산 실수 (음수 처리)
3. 문제 잘못 이해 (쪼개지면서 바로 움직여버림)
4. 문제 잘못 이해 (전부 대각일 경우 누락)
*/
