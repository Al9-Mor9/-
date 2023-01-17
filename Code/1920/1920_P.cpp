#include <iostream>
#include <set>
using namespace std;

int N, M, n;
set<int> s;
int main(){
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &n);
        if (!s.count(n)) s.insert(n);
    }
    scanf("%d", &M);
    for (int i = 0; i < M; i++){
        scanf("%d", &n);
        printf("%d\n", s.count(n));        
    }
    
}
