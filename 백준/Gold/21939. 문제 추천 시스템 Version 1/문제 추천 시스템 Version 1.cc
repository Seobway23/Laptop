#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    set<pair<int, int>> s; // (난이도, 문제번호)
    unordered_map<int, int> level; // 문제번호 → 난이도

    for (int i = 0; i < n; i++) {
        int p, l;
        cin >> p >> l;
        s.insert({l, p});
        level[p] = l;
    }

    int m;
    cin >> m;
    while (m--) {
        string cmd;
        cin >> cmd;
        if (cmd == "recommend") {
            int x;
            cin >> x;
            if (x == 1) cout << (*s.rbegin()).second << '\n';
            else cout << (*s.begin()).second << '\n';
        } else if (cmd == "add") {
            int p, l;
            cin >> p >> l;
            s.insert({l, p});
            level[p] = l;
        } else if (cmd == "solved") {
            int p;
            cin >> p;
            s.erase({level[p], p});
            level.erase(p);
        }
    }
}
