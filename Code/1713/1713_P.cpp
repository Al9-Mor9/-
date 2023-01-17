#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int main(){
    int N, M, rec[1000], student[101] = {0, };
    priority_queue<pair<int, int>, vector<pair<int,int>>, greater<>> pq;
    queue<pair<int,int>> tmp;
    vector<int> ans;

    scanf("%d%d", &N, &M);
    for (int i = 0; i < M; i++){
        scanf("%d", &rec[i]);
        if (!student[rec[i]]){
            if ((int)pq.size() == N) {
                student[rec[pq.top().second]] = 0;
                pq.pop();
            }
            pq.push({++student[rec[i]], i});
        }
        else {
            while (rec[pq.top().second] != rec[i]){    
                tmp.push(pq.top());
                pq.pop();
            }
            int idx = pq.top().second;
            pq.pop();
            pq.push({++student[rec[i]], idx});
            while (!tmp.empty()){
                pq.push(tmp.front());
                tmp.pop();
            }
        }
    }

    while (!pq.empty()){
        ans.push_back(rec[pq.top().second]);
        pq.pop();
    } 

    sort(ans.begin(), ans.end());
    for (int a : ans) printf("%d ", a);


}
