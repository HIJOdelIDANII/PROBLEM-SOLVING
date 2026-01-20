#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;

    vector<int> riddles(n);
    for(int i = 0; i < n; i++){
        int mask = 0;
        for(int j = 0; j < k; j++){
            int input;
            cin >> input;
            if(input) {
                mask |= (1 << j);
            }
        }
        riddles[i] = mask;
    }

    for(int subset = 1; subset < (1 << n); subset++){
        int total = __builtin_popcount(subset);
        vector<int> teamKnows(k, 0);

        for(int i = 0; i < n; i++){
            if(subset & (1 << i)){
                for(int j = 0; j < k; j++){
                    if(riddles[i] & (1 << j)){
                        teamKnows[j]++;
                    }
                }
            }
        }

        bool valid = true;
        for(int j = 0; j < k; j++){
            if(teamKnows[j] * 2 > total){
                valid = false;
                break;
            }
        }

        if(valid){
            cout << "YES\n";
            return;
        }
    }

    cout << "NO\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}