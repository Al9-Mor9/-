#include <iostream>
#include <string.h>
#include <queue>
#include <set>
using namespace std;

string N;
int K, len, ans = 0;
queue<pair<string, int>> q;
set<pair<string, int>> s;

void bfs(){
    while (!q.empty()){
        pair<string, int> tmp = q.front();
        if (tmp.second == K){
            ans = max(ans, stoi(q.front().first));
            q.pop();
            continue;
        }
        q.pop();
        for (int i = 0; i < N.length(); i++){
            for (int j = i + 1; j < N.length(); j++){
                swap(tmp.first[i], tmp.first[j]);
                if (!s.count({tmp.first, tmp.second + 1})) {
                    s.insert({tmp.first, tmp.second + 1});
                    q.push({tmp.first, tmp.second +1});
                }
                swap(tmp.first[i], tmp.first[j]);
            }
        }               
    }
}

int main(){
    cin >> N >> K;
    len = (int)N.length();
    if (len == 1 || (len == 2 && N[1] == '0')) printf("-1");
    else {
        q.push({N, 0});
        bfs();
        printf("%d", ans);
    }

}
