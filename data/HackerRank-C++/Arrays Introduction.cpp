#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int i, n;
    cin >> n;
    int a[n];
    for (i = 0; i < n; i++)
        cin >> a[i];
    for (i = n - 1; i > -1; i--)
        cout << a[i] << ' ';
    return 0;
}
