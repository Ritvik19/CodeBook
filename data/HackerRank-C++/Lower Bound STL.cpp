#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> v;
    int n, x, q, y;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> x;
        v.push_back(x);
    }
    cin >> q;
    for (int i = 0; i < q; i++)
    {
        cin >> y;
        vector<int>::iterator low = lower_bound(v.begin(), v.end(), y);
        if (v[low - v.begin()] == y)
            cout << "Yes " << (low - v.begin() + 1) << endl;
        else
            cout << "No " << (low - v.begin() + 1) << endl;
    }

    return 0;
}
