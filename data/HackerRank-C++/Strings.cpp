#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a, b;
    cin >> a >> b;
    cout << a.length() << ' ' << b.length() << endl;
    cout << a + b << endl;
    cout << b.at(0) << a.substr(1) << ' ';
    cout << a.at(0) << b.substr(1) << endl;
    return 0;
}