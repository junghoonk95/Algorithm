#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, M, K;
vector<int> r, c, m, s, d;
class ball
{
public:
    int r, c, m, s, d;
};
int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};
vector<ball> map[51][51];
vector<ball> balls;
bool dir(int x, int y);
void input()
{
    int tmp;
    cin >> N >> M >> K;
    for (int i = 0; i < M; i++)
    {
        ball b;
        cin >> b.r >> b.c >> b.m >> b.s >> b.d;
        balls.push_back(b);
    }
}
void move()
{
    // map 초기화
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            map[i][j].clear();
        }
    }
    // ball traverse
    for (int i = 0; i < balls.size(); i++)
    {
        int next_r = balls[i].r + (balls[i].s * dx[balls[i].d]);
        int next_c = balls[i].c + (balls[i].s * dy[balls[i].d]);
        while (next_r < 1)
            next_r += N;
        while (next_c < 1)
            next_c += N;
        while (next_r > N)
            next_r -= N;
        while (next_c > N)
            next_c -= N;

        ball b_tmp = balls[i];
        b_tmp.r = next_r;
        b_tmp.c = next_c;
        map[next_r][next_c].push_back(b_tmp);
    }
}
void jam()
{
    vector<ball> tmp;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            if (map[i][j].size() == 1)
            {
                tmp.push_back(map[i][j][0]);
            }
            else if (map[i][j].size() >= 2)
            {
                int tol_m = 0, tol_s = 0;
                for (int k = 0; k < map[i][j].size(); k++)
                {
                    tol_m += map[i][j][k].m;
                    tol_s += map[i][j][k].s;
                }
                ball nb;
                nb.r = i;
                nb.c = j;
                nb.m = tol_m / 5;
                nb.s = tol_s / map[i][j].size();
                if (nb.m > 0)
                {
                    // whether odd or even
                    if (dir(i, j))
                    {
                        nb.d = 0;
                        tmp.push_back(nb);
                        nb.d = 2;
                        tmp.push_back(nb);
                        nb.d = 4;
                        tmp.push_back(nb);
                        nb.d = 6;
                        tmp.push_back(nb);
                    }
                    else
                    {
                        nb.d = 1;
                        tmp.push_back(nb);
                        nb.d = 3;
                        tmp.push_back(nb);
                        nb.d = 5;
                        tmp.push_back(nb);
                        nb.d = 7;
                        tmp.push_back(nb);
                    }
                }
            }
        }
    }
    balls = tmp;
}
bool dir(int x, int y)
{
    bool flag;
    // odd false, even true
    if (map[x][y][0].d % 2 == 0)
    {
        flag = true;
    }
    else
    {
        flag = false;
    }
    for (int k = 1; k < map[x][y].size(); k++)
    {
        if (map[x][y][k].d % 2 == 0 && flag == false)
        {
            return false;
        }
        else if (map[x][y][k].d % 2 == 1 && flag == true)
        {
            return false;
        }
    }
    return true;
}
void solution()
{
    for (int i = 0; i < K; i++)
    {
        move();
        jam();
    }
    // output
    int result = 0;
    for (int j = 0; j < balls.size(); j++)
    {
        result += balls[j].m;
    }
    cout << result;
}
int main()
{
    input();
    solution();
}
