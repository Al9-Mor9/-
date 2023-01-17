#include <iostream>
#include <queue>
using namespace std;

int R, C, c;
char forest[50][50];
pair<int,int> startPos, destPos;
int dir[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

int bfs(char prev[50][50], int cnt){
    if (prev[destPos.first][destPos.second] == 'S') return cnt;
    char tmp[50][50] = {0, };
    for (int i = 0; i < R; i++){
        for (int j = 0; j < C; j++){
            if (prev[i][j] == '*') {
                tmp[i][j] = '*';
                for (int k = 0; k < 4; k++){
                    if (i + dir[k][0] >= 0 && i + dir[k][0] < R && j + dir[k][1] >= 0 && j + dir[k][1] < C) {
                        if (prev[i + dir[k][0]][j + dir[k][1]] != 'D' && prev[i + dir[k][0]][j + dir[k][1]] != 'X') tmp[i + dir[k][0]][j + dir[k][1]] = '*';
                    }
                }
            }
            else if (tmp[i][j] != '*') tmp[i][j] = prev[i][j];
        }
    }
    bool movable = false;
    for (int i = 0; i < R; i++){
        for (int j = 0; j < C; j++){
            if (prev[i][j] == 'S') {
                for (int k = 0; k < 4; k++){
                    if (i + dir[k][0] >= 0 && i + dir[k][0] < R && j + dir[k][1] >= 0 && j + dir[k][1] < C) {
                        if (tmp[i + dir[k][0]][j + dir[k][1]] == '.' || tmp[i + dir[k][0]][j + dir[k][1]] == 'D' ) {
                            tmp[i + dir[k][0]][j + dir[k][1]] = 'S';
                            movable = true;
                        }
                    }
                }
            }
        }
    }

    if (!movable) return -1;
    else return bfs(tmp, cnt + 1);    

}


int main(){
    scanf("%d%d", &R, &C);
    for (int i = 0; i < R; i++){
        for (int j = 0; j < C; j++){
            scanf("\n%c", &forest[i][j]);
            if (forest[i][j] == 'S') startPos = {i, j};
            else if (forest[i][j] == 'D') destPos = {i, j};           
        }
    }
    int ans = bfs(forest, 0);
    if (ans > 0) printf("%d", ans);
    else printf("KAKTUS");
}
