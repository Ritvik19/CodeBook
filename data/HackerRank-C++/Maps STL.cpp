#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int main()
{
    map<string, int> m;
    int q, t, y;
    string x;
    cin >> q;
    for (int i = 0; i < q; i++)
    {
        cin >> t >> x;
        switch (t)
        {
        case 1:
            cin >> y;
            m[x] += y;
            break;
        case 2:
            m.erase(x);
            break;
        case 3:
            cout << m[x] << endl;
            break;
        }
    }

    return 0;
}
