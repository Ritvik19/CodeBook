#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;

int main()
{
    set<int> s;
    int q, x, y;
    cin >> q;
    for (int i = 0; i < q; i++)
    {
        cin >> x >> y;
        switch (x)
        {
        case 1:
            s.insert(y);
            break;
        case 2:
            s.erase(y);
            break;
        case 3:
            set<int>::iterator itr = s.find(y);
            if (itr == s.end())
                cout << "No" << endl;
            else
                cout << "Yes" << endl;
        }
    }
    return 0;
}
