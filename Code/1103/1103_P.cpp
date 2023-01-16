#include <iostream>
using namespace std;

int N, M, ans = 0;
char board[50][51];
int dir[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
int dp[50][50] = {0, };
bool visited[50][50] = {false, };


void dfs(int x, int y, int cnt){
    if (ans == -1) return;
    if (dp[x][y] >= cnt) return;
    if (visited[x][y]) {
        ans = -1; 
        return;
    }
    ans = ans > cnt ? ans : cnt;
    dp[x][y] = cnt;
    visited[x][y] = true;
    int amt = board[x][y] - '0';
    for (int i = 0; i < 4; i++){
        int nextX = x + amt * dir[i][0];
        int nextY = y + amt * dir[i][1];
        if (nextX < 0 || nextX >= N || nextY < 0 || nextY >= M || board[nextX][nextY] == 'H') continue;
        dfs(nextX, nextY, cnt + 1);
    }
    visited[x][y] = false;
}


int main(){
    scanf("%d%d", &N, &M);
    for (int i = 0; i < N; i++) {
        scanf("%s", board[i]);
    }
    dfs(0, 0, 1);
    printf("%d", ans);
}
