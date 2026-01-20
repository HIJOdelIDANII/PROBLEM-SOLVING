
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;
const int MAXN = 1000005; // Set this to the maximum N in the problem

long long fact[MAXN];
long long invFact[MAXN];
long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD; // Change MOD if needed
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}
// This function must be called once in main() before using nCr
void precompute() {
    fact[0] = 1;
    for (int i = 1; i < MAXN; i++) {
        fact[i] = (fact[i - 1] * i) % MOD;
    }

    // Compute modular inverse of the last factorial using Fermat's Little Theorem
    invFact[MAXN - 1] = power(fact[MAXN - 1], MOD - 2); 
    
    // Fill the rest of the inverse factorials backwards
    for (int i = MAXN - 2; i >= 0; i--) {
        invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
    }
}

// Your updated nCr function
long long nCr(int n, int r) {
    if (r < 0 || r > n) return 0;
    return (((fact[n] * invFact[r]) % MOD) * invFact[n - r]) % MOD;
}

struct DSU {
    vector<int> parent;
    vector<int> size;
    
    DSU(int n) {
        parent.resize(n + 1);
        size.resize(n + 1, 1);
        for(int i = 0; i <= n; i++) parent[i] = i;
    }
    
    int find(int v) {
        if (v == parent[v]) return v;
        return parent[v] = find(parent[v]); // Path compression
    }
    
    void unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b) {
            if (size[a] < size[b]) swap(a, b); // Union by size
            parent[b] = a;
            size[a] += size[b];
        }
    }
};
// Usage: DSU dsu(n); dsu.unite(1, 2); if(dsu.find(1) == dsu.find(2)) ...



long long modInverse(long long n) {
    return power(n, MOD - 2);
}

void bfs(int start, int n, vector<vector<int>>& adj) {
    vector<int> dist(n + 1, -1);
    queue<int> q;
    
    dist[start] = 0;
    q.push(start);
    
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        
        for (int v : adj[u]) {
            if (dist[v] == -1) { // Not visited
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
}

struct FenwickTree {
    int n;
    vector<long long> tree;
    
    FenwickTree(int n) : n(n), tree(n + 1, 0) {}
    
    void add(int idx, int delta) {
        for (; idx <= n; idx += idx & -idx) 
            tree[idx] += delta;
    }
    
    long long query(int idx) {
        long long sum = 0;
        for (; idx > 0; idx -= idx & -idx) 
            sum += tree[idx];
        return sum;
    }
    
    // Returns sum from l to r
    long long query(int l, int r) {
        return query(r) - query(l - 1);
    }
};
// Usage: FenwickTree ft(n); ft.add(index, value); ft.query(l, r);

vector<bool> is_prime;
void sieve(int max_n) {
    is_prime.assign(max_n + 1, true);
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p * p <= max_n; p++) {
        if (is_prime[p]) {
            for (int i = p * p; i <= max_n; i += p)
                is_prime[i] = false;
        }
    }
}

long long gcd(long long a, long long b) {
    return b == 0 ? a : gcd(b, a % b);
}

long long lcm(long long a, long long b) {
    return (a / gcd(a, b)) * b; // Divide first to avoid overflow
}


void solve() {
    int n, t;
    cin >> n >> t;
    vector<pair<int, int>> h(n);
    for(int i = 0; i < n; i++)
    {
        cin >> h[i].first >> h[i].second;
    }
    sort(h.begin(), h.end());
    int res = 2;
    for(int j = 0; j < n-1; j++)
    {
        float z = h[j+1].first - h[j].first - (float)h[j+1].second/2 - (float)h[j].second/2;
        if (z > t)
        {
            res += 2;
        }
        else if (z == t)
        {
            res += 1;
        }
    }
    cout << res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    solve();
    return 0;
}