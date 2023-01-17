#include <iostream>
#include <vector>
using namespace std;

int chiMap[50][50];
vector<pair<int,int>> houses, chickens;

int getChickenDist(vector<pair<int,int>> chickens){
    int chickenDist = 0;
    for (pair<int, int> house : houses){
        int dist = 2147483647;
        for (pair <int, int> chicken : chickens){
            dist = min(dist, abs(chicken.first - house.first) + abs(chicken.second - house.second));
        }
        chickenDist += dist;
    }
    return chickenDist;
}

int main(){
    int N, M, ans = 2147483647;
    scanf("%d%d", &N, &M);
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            scanf("%d", &chiMap[i][j]);
            if (chiMap[i][j] == 1) houses.push_back({i, j});
            else if (chiMap[i][j] == 2) chickens.push_back({i, j});
        }
    }    

    for (int i = 0; i < (1 << (chickens.size() + 1) -1); i++){
        vector<pair<int,int>> tmp;
        for (int j = 0; j < (chickens.size()); j++){
            if (i & (1 << j)){
                tmp.push_back(chickens[j]);
            }   
        }
        if (tmp.size() == M) ans = min(ans, getChickenDist(tmp));
    }
    printf("%d", ans);

}
